from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
def open_file():
    pth = askopenfilename(
        filetypes = [("text files","*.txt"),("All file","*.*")]
    )
    if not pth:
        return text_edit.delete(1.0,END)
    with open(pth,"r") as input_file:
        txt = input_file.read()
        text_edit.insert(END,txt)
    window.title(f"Text Editor :- {pth}")
def save_fileas():
    pth = asksaveasfilename(
        defaultextension = "txt",
        filetypes =[("text files","*.txt"),("All files","*.*")],
    )
    if not pth:
        return
    with open(pth,"w") as output:
        txt = text_edit.get(1.0,END)
        output.write(txt)
    window.title(f"Text Editor :- {pth}")
def save_file():
    pth = "C:\\Users\\rahma\\OneDrive\\Desktop\\text.txt"
    if not pth:
        return
    with open(pth,"w") as out:
        txt = text_edit.get(1.0,END)
        out.write(txt)
        window.title(f"Text Editor :- {pth}")
window = Tk()
window.title("Text Editor")
window.resizable(1,1)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry(f"{int(w)}x{int(h)}")
# window.iconbitmap("k.ico")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
text_edit = Text(window,font=("times new roman",20,"bold"),fg="white",bg="gray")
fr_button = Frame(window,relief=GROOVE,bd=2,bg="skyblue")
btn_open = Button(fr_button,text="Open",command=open_file,fg="blue",bg="lime",font=("times new roman",12,"bold"))
btn_saveas = Button(fr_button,text="Save as",command=save_fileas,fg="blue",bg="lime",font=("times new roman",12,"bold"))
btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_saveas.grid(row=2,column=0,sticky="ew",padx=5,pady=5)
fr_button.grid(row=0,column=0,sticky="ns")
text_edit.grid(row=0,column=1,sticky="nsew")
btn_save = Button(fr_button,text="Save",command=save_file,fg="blue",bg="lime",font=("times new roman",12,"bold"))
btn_save.grid(row=1,column=0,sticky="ew",padx=5,pady=5)
window.mainloop()
