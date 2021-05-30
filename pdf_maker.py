import os
import img2pdf
from PIL import Image
from PyPDF2 import PdfFileMerger
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename,askopenfilenames
'''pdfs = ['E:\\file.pdf','E:\\Python.pdf']
merger = PdfFileMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write("result.pdf")
merger.close()
print('success')'''
t = 0
path_file = ''
lst = []
fresh = []
pdfs = []
psave = ''
def select():
    global t
    r = radio.get()
    if r == 1:
        txt.set('select folder:')
        add.set('Add Folder')
        t = r
        add_btn.configure(state=ACTIVE)
    elif r == 2:
        txt.set('select one file:')
        add.set('Add one file')
        t = r
        add_btn.configure(state=ACTIVE)
    elif r == 3:
        txt.set('select files:')
        add.set('Add files')
        t = r
        add_btn.configure(state=ACTIVE)
    else:
        add_btn.configure(state=DISABLED)
        add.set('Add')
        txt.set('select type from above:')
        subs()
def ask():
    global path_file
    global lst
    global fresh
    if t == 1:
        path_file = askdirectory()
        pth.set(path_file)
        ch = os.chdir(path_file)
        collec = os.listdir(ch)
        for file in collec:
            if file not in lst:
                lst.append(file)
            else:
                pass
    elif t == 2:
        path_file = askopenfilename()
        pth.set(path_file)
        if path_file not in lst:
            lst.append(path_file)
        else:
            pass
    elif t == 3:
        path_file = askopenfilenames()
        pth.set(path_file)
        for i in path_file:
            if i not in lst:
                lst.append(i)
            else:
                pass
    for j in lst:
        if j not in fresh:
            fresh.append(j)
            convert_btn.configure(state=ACTIVE)
def subs():
    for k in fresh:
        lst_box.insert(END,k)
def select_path():
    global psave
    psave = askdirectory()
    if psave:
        pth_save.set(psave)
    else:
        pth_save.set('please select path to save pdf file!')
def convert():
    global fresh
    global psave
    ent = etry.get()
    if psave:
        image = Image.open(f"{pth_save.get()}/{fresh[1]}")
        byte = image.convert('RGB')
        if ent:
            byte.save(f"{psave}/{ent}.pdf")
        else:
            byte.save(f"{psave}/result.pdf")
    else:
        pass
window = Tk()
window.geometry('850x550+350+50')
window.resizable(0,0)
window.title('PDF Maker')
window.configure(background='skyblue')
radio = IntVar()
txt = StringVar()
add = StringVar()
pth = StringVar()
fname = StringVar()
etry = StringVar()
pth_save = StringVar()
r1 = Radiobutton(window,value=1,variable=radio,command=select,text='Folder',activebackground='skyblue',bg='skyblue',font=('times new roman',15,'bold'),activeforeground='blue')
r1.grid(row=0,column=0,padx=20,pady=20)
r2 = Radiobutton(window,value=2,variable=radio,command=select,text='One file',activebackground='skyblue',bg='skyblue',font=('times new roman',15,'bold'),activeforeground='blue')
r2.grid(row=0,column=1,padx=20,pady=20)
r3 = Radiobutton(window,value=3,variable=radio,command=select,text='Files',activebackground='skyblue',bg='skyblue',font=('times new roman',15,'bold'),activeforeground='blue')
r3.grid(row=0,column=2,padx=20,pady=20)
r4 = Radiobutton(window,value=4,variable=radio,command=select,text='Insert',activebackground='skyblue',bg='skyblue',font=('times new roman',15,'bold'),activeforeground='blue')
r4.grid(row=0,column=3,padx=20,pady=20)
label = Label(window,width=20,textvariable=txt,font=('times new roman',15,'bold'),bg='skyblue',fg='red')
label.grid(row=1,column=0,padx=20,pady=20)
txt.set('select type from above:')
save_label = Label(window,width=20,text='select save directory:',font=('times new roman',15,'bold'),bg='skyblue',fg='red')
save_label.grid(row=2,column=0,pady=20)
add_btn = Button(window,textvariable=add,command=ask,width=10,font=('times new roman',15,'bold'),bg='skyblue',fg='red',bd=5,relief=GROOVE,state=DISABLED,activeforeground='red',activebackground='skyblue')
add_btn.grid(row=1,column=3,pady=20)
path_label = Label(window,textvariable=pth,width=25,height=1,font=('times new roman',15,'bold'),bg='white',fg='red')
path_label.grid(row=1,column=1,pady=20)
add.set('Add')
path_save = Label(window,textvariable=pth_save,width=25,height=1,font=('times new roman',15,'bold'),bg='white',fg='red')
path_save.grid(row=2,column=1,pady=20)
path_btn = Button(window,text='select',command=select_path,width=10,font=('times new roman',15,'bold'),bg='skyblue',fg='red',bd=5,relief=GROOVE,activeforeground='red',activebackground='skyblue')
path_btn.grid(row=2,column=3,pady=20)
fr =LabelFrame(window,width=530,height=350,bg='yellow',fg='red')
fr.place(x=30,y=250)
scr = Scrollbar(fr,orient=VERTICAL)
lst_box =Listbox(fr,bg='skyblue',fg='red',bd=5,width=60,height=11,yscrollcommand=scr.set,font=('times new roman',15,'bold'))
scr.pack(side=RIGHT,fill=Y)
scr.config(command=lst_box.yview)
lst_box.pack(fill=BOTH)
file_name = Label(window,width=14,textvariable=fname,font=('times new roman',15,'bold'),bg='skyblue',fg='red')
file_name.place(x=670,y=270)
fname.set('Enter pdf file name:')
entry = Entry(window,width=19,textvariable=etry,font=('times new roman',13,'bold'),bg='white',fg='red')
entry.place(x=670,y=300)
convert_btn = Button(window,text='Save',command=convert,width=10,font=('times new roman',15,'bold'),bg='skyblue',fg='red',bd=5,relief=GROOVE,state=DISABLED,activeforeground='red',activebackground='skyblue')
convert_btn.place(x=685,y=340)
window.mainloop()