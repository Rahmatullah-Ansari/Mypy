from pdf2docx import Converter,parse
from tkinter.filedialog import askopenfile
from tkinter import *
from datetime import datetime
import os
# file_name='python.pdf'
# word_file='output.docx'
#covertor method use.
# cvrt=Converter(file_name)
# cvrt.convert(word_file,start=0,end=None)
# cvrt.close()
#second method parse method.
# parse(file_name,word_file,start=0,end=None)
file_name=""
def select_file():
    global file_name
    try:
        file_name=askopenfile(mode='r',title="open file",filetypes=[("Pdf File","*.pdf"),("All Files","*.*")])
        f=(file_name.name).split("/")[-1]
        txt.set(f)
        btn1.config(state="active")
    except:
        txt.set("No file selected!")
        btn1.config(state=DISABLED)
def convert_file():
    global file_name
    hr=datetime.now().hour
    mn=datetime.now().minute
    sec=datetime.now().second
    out=f"{hr} {mn} {sec}.docx"
    try:
        txt1.set("Converting...")
        # parse(file_name,out,start=0,end=None)
        cvrt=Converter(file_name)
        cvrt.convert(out,start=0,end=None)
        cvrt.close()
        txt1.set("Coverted.")
        lbl1.config(fg="green")
        btn1.config(state=DISABLED)
        txt.set("")
    except:
        txt1.set("Failed!")
        lbl1.config(fg="red")
window=Tk()
window.title("PDF 2 DOCX")
window.geometry("500x250+50+50")
window.resizable(0,0)
window.config(bg="skyblue")
txt=StringVar()
txt1=StringVar()
btn=Button(window,text="Select file",font=("Times new roman",20,"bold"),command=select_file)
btn.place(x=20,y=20)
lbl=Label(window,textvariable=txt,width=15,font=("Times new roman",20,"bold"))
lbl.place(x=210,y=30)
lbl1=Label(window,textvariable=txt1,width=20,font=("Times new roman",20,"bold"))
lbl1.place(x=100,y=100)
btn1=Button(window,text="Convert",font=("Times new roman",20,"bold"),command=convert_file)
btn1.place(x=190,y=150)
mainloop()

