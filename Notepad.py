from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox,colorchooser
from tkinter.ttk import *
import webbrowser
from datetime import datetime
file = 'No File'
fi = 25
font_i = True
yes = False
font_f = ""
font_s = ""
font_si=0
def help_me():
    webbrowser.open("https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA")
def about():
    messagebox.showinfo("About Notepad","This Notepad is developed by Rahmatullah Ansari\nEmail-id :- rahmatullahansari38@gmail.com\nContact No. :- 9752078964")
def open_file(event=False):
    try:
        global file
        txtarea.delete(1.0,END)
        pth = askopenfile(initialdir="/",title="Open File",filetypes=[("Text File","*.txt"),("All Files","*.*")])
        for data in pth:
            txtarea.insert(INSERT,data)
        x =txtarea.get(1.0,END)
        file = pth.name
        window.title(f"Notepad :- {pth.name}")
    except Exception as ex:
        pass
def save_as(event=False):
    try:
        pth = asksaveasfile(mode="w",defaultextension="txt",filetypes=[("Text File","*.txt"),("All Files","*.*")])
        data = txtarea.get(1.0,END)
        pth.write(data)
        global file
        file =pth.name
        window.title(f"Notepad  :-  {file}")
        pth.close()
    except Exception as ex:
        pass
def save_file(event=False):
    global file
    global yes
    try:
        if file=="No File":
            window.title("Notepad")
            save_as()
            yes=True
        else:
            f=open(file,mode='r+')
            f.seek(0)
            f.truncate()
            f.close()
            f = open(file,mode="w")
            window.title(f"Notepad  :-  {file}")
            f.write(txtarea.get(1.0,END))
            f.close()
            yes = True
    except Exception as ex:
        pass
def clear():
    try:
        txtarea.delete(1.0,END)
    except:
        pass
def exit(event=False):
    global file
    global yes
    val = txtarea.get(1.0,END)
    if not val.strip():
        window.destroy()
    elif file:
        if yes:
            window.destroy()
            yes = False
        else:
            result = messagebox.askyesnocancel("Save Dialog Box","Do you want to save this file?")
            if result == True:
                save_file()
                yes = False
                window.destroy()
            elif result == None:
                pass
            else:
                yes = False
                window.destroy()
    else:
        result = messagebox.askyesnocancel("Save Dialog Box","Do you want to save this file?")
        if result==True:            
            save_as()
            yes = False
            window.destroy()
        elif result == None:
            pass
        else:
            yes = False
            window.destroy()
def new_file(event=False):
    global file,yes
    window.title("*Notepad")
    val = txtarea.get(1.0,END)
    if not val.strip():
        file="No File"
        yes=False
        clear()
    elif not yes:
        result = messagebox.askyesnocancel("Save Dialog Box","Do you want to save this file?")
        if result==True:
            save_file()
            window.title(f"Notepad  :-  {file}")
            clear()
            file="No File"
            window.title("Notepad")
        elif result == False:
            clear()
            yes=False
            file="No File"
            window.title("Notepad")
    else:
        save_file()
        window.title("Notepad")
        clear()
        file="No File"
        yes=False
def new_window(event=False):
    pass
def inc(event=False):
    global font_s,font_f,font_si,font_i
    global fi
    if not font_i:
        fi = int(font_si)
        if fi >= 10:
            if fi <= 116:
                fi += 1
                txtarea.config(font=(f"{font_f}",fi,f"{font_s}"))
                font_i=True
            else:
                font_i = True
                pass
    else:
        if fi >= 10:
            if fi <= 116:
                fi += 1
                txtarea.config(font=(f"{font_f}",fi,f"{font_s}"))
            else:
                pass
def dec(event=False):
    global font_s,font_f,font_si,font_i
    global fi
    if not font_i:
        fi = int(font_si)
        if fi <= 116:
            if fi > 10:
                fi -= 1
                txtarea.config(font=(f"{font_f}",fi,f"{font_s}"))
                font_i=True
            else:
                font_i = True
                pass
    else:
        if fi <= 117:
            if fi > 10:
                fi -= 1
                txtarea.config(font=(f"{font_f}",fi,f"{font_s}"))
            else:
                pass
def df(event=False):
    global fi
    txtarea.config(font=("Arial",25,"bold"))
    fi = 25
def copy(event=False):
    try:
        txtarea.clipboard_clear()
        txtarea.clipboard_append(txtarea.selection_get())
    except Exception as ex:
        pass
def paste(event=False):
    try:
        txtarea.insert(INSERT,txtarea.selection_get())
    except Exception as ex:
        pass
def cut(event=False):
    try:
        txtarea.delete('sel.first','sel.last')
    except Exception as ex:
        pass
def delete(event=False):
    try:
        txtarea.delete('sel.first','sel.last')
    except Exception as ex:
        pass
def un(event=False):
    try:
        txtarea.edit_undo
    except:
        pass
def rd(event=False):
    try:
        txtarea.edit_redo
    except:
        pass
def bgcolor():
    c = colorchooser.askcolor()
    txtarea.config(bg=c[1])
def fgcolor():
    c = colorchooser.askcolor()
    txtarea.config(fg=c[1])
def wr():
    if ch.get() == 1:
        txtarea.config(wrap=WORD)
    elif ch.get == 0:
        txtarea.config(wrap=None)
def search(event=False):
    try:
        webbrowser.open(f"https://www.google.com/search?q={txtarea.selection_get()}&rlz=1C1ONGR_enIN932IN932&oq={txtarea.selection_get()}&aqs=chrome..69i57j46i433j0i433j46i433j46i395i433j0i10i395i433j69i60l2.1831j1j7&sourceid=chrome&ie=UTF-8")
    except:
        pass
def sel(event=False):
    txtarea.tag_add(SEL, "1.0", END)
def td(event=False):
    h = datetime.now().hour
    m = datetime.now().minute
    x = datetime.now()
    mn=x.month
    y=x.year
    d=x.day
    if h < 12:
        txtarea.insert(INSERT,f"{h}:{m} AM {d}-{mn}-{y}")
    elif h == 12:
        txtarea.insert(INSERT,f"{h}:{m} PM {d}-{mn}-{y}")
    elif h > 12:
        txtarea.insert(INSERT,f"{h-12}:{m} PM {d}-{mn}-{y}")
flag = True
def st():
    global flag
    flag = True
def fnt():
    global flag
    if flag:
        def ok():
            global font_s,font_f,font_si,font_i
            try:
                v1 = fn.get()
                v2 = fs.get()
                v3 = s.get()
                font_f = v1
                font_s = v2
                font_si = v3
                font_i = False
                if v1 == '' and v2 == '' and v3 == '':
                    messagebox.showwarning("Select","Please select the field!!")
                elif v1 != '' or v2 != '' or v3 != '':
                    txtarea.config(font=(f"{v1}",v3,f"{v2}"))
                    fn.current(v1)
                    fs.current(v2)
                    s.current(v3)
            except Exception as ex:
                pass
            st()
            f.destroy()
        def cancel():
            st()
            f.destroy()
        def check(event=False):
            v1 = fn.get()
            v2 = fs.get()
            v3 = s.get()
            e.config(font=(f"{v1}",v3,f"{v2}"))
        f=Tk()
        f.title("Font Setup")
        f.geometry("610x500+250+170")
        f.iconbitmap("note.ico")
        f.config(background="skyblue")
        a =Label(f,text="Font",font=("Arial",15,"bold"),foreground="red",background="skyblue")
        a.place(x=50,y=30)
        lst2=[]
        for i in range(8,116):
            lst2.append(i)
        fn = Combobox(f,height=9)
        fn.bind("<<ComboboxSelected>>",check)
        fn['values']=("Consolas","Arial","Bahnschrift",
        "Calibri","Cambria","Cambria Math",
        "Candara","Comic sans MS","Constania",
        "Corbel","Courier","Courier New","Ebrima",
        "Fixedsys","Franklin Gothic","Gabriola",
        "Gadugi","Georgia","HoloLens MDL2 Assets",
        "Impact","Ink Free","Javanese Text",
        "Leelawadee UI","Lucida Console",
        "Lucida Sans Unicode","Malgun Gothic",
        "Marlett","Microsoft Himalya",
        "Microsoft JhengHei","Microsoft JhengHei UI",
        "Microsoft New Tai Lue","Microsoft PhagsPa",
        "Microsoft Sans Serif","Microsoft Tai Le",
        "Microsoft YaHei","Microsoft YaHei UI",
        "Microsoft Yi Baiti","Roman","Segoe UI",
        "Segoe UI Emoji")
        fn.place(x=50,y=60,width=160,height=20)
        fn.current(0)
        b =Label(f,text="Font Style",font=("Arial",15,"bold"),foreground="red",background="skyblue")
        b.place(x=220,y=30)
        fs = Combobox(f,height=9)
        fs['values'] = ("normal","bold","roman","italic","underline","overstrike")
        fs.current(0)
        fs.bind("<<ComboboxSelected>>",check)
        fs.place(x=220,y=60,width=160,height=20)
        c =Label(f,text="Size",font=("Arial",15,"bold"),foreground="red",background="skyblue")
        c.place(x=400,y=30)
        s = Combobox(f,values=lst2,height=7)
        s.current(0)
        s.bind("<<ComboboxSelected>>",check)
        s.place(x=400,y=60,width=160,height=20)
        d =Label(f,text="Sample",font=("Arial",15,"bold"),foreground="red",background="skyblue")
        d.place(x=300,y=270)
        e =Label(f,text="Abcd",font=("Arial",20,"bold"),foreground="red")
        e.place(x=300,y=310,width=230,height=100)
        btn1 = Button(f,text="Cancel",command=cancel)
        btn1.place(x=430,y=450)
        btn2 = Button(f,text="Ok",command=ok)
        btn2.place(x=300,y=450)
        f.resizable(0,0)
        flag=False
        f.mainloop()
    else:
        messagebox.showinfo("Page Setup","Page Setup is already opened!")
window = Tk()
window.title("Notepad")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry("700x700+200+50")
window.iconbitmap("note.ico")
window.rowconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
txtarea = Text(window,padx=15,wrap=WORD,bg='white',fg='black',pady=15,font=("Franklin Gothic",25,"bold"),selectbackground="blue",bd=5,insertwidth=2,undo=True)
txtarea.place(x=0,y=0,width=int(w)-10,height=int(h)-98)
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
# attach textbox to scrollbar
txtarea.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txtarea.yview)
# sc = Scrollbar(window)
# sc.pack(side=BOTTOM,fill=X)
# txtarea.config(xscrollcommand=sc.set)
# sc.config(command=txtarea.xview)
#creating menu bar.
menu = Menu()
window.config(menu=menu)
window.bind("<Control-o>",open_file)
window.bind("<Control-O>",open_file)
window.bind("<Control-s>",save_file)
window.bind("<Control-S>",save_file)
window.bind("<Control-n>",new_file)
window.bind("<Control-N>",new_file)
window.bind("<Control-Shift-N>",new_window)
window.bind("<Control-Shift-n>",new_window)
window.bind("<Control-c>",copy)
window.bind("<Control-C>",copy)
window.bind("<Control-V>",paste)
window.bind("<Control-v>",paste)
window.bind("<Control-Shift-S>",save_as)
window.bind("<Control-Shift-s>",save_as)
window.bind("<Control-x>",cut,copy)
window.bind("<Control-X>",cut,copy)
window.bind("<Delete>",delete)
window.bind("<Control-z>",un)
window.bind("<Control-Z>",un)
window.bind("<Control-R>",rd)
window.bind("<Control-r>",rd)
window.bind("<Control-=>",inc)
window.bind("<Control-d>",dec)
window.bind("<Control-D>",dec)
window.bind("<Control-0>",df)
window.bind("<Control-E>",search)
window.bind("<Control-e>",search)
window.bind("<Control-A>",sel)
window.bind("<Control-a>",sel)
window.bind("<F2>",exit)
window.bind("<F5>",td)
window.protocol("WM_DELETE_WINDOW",exit)
mb = Menu(menu,tearoff=False)
menu.add_cascade(label="File",menu=mb)
mb.add_command(label="New",accelerator="Ctrl+N",command=new_file)
# mb.add_command(label="New Window",command=new_window,accelerator="Ctrl+Shift+N")
mb.add_command(label="Open",accelerator="Ctrl+O",command=open_file)
mb.add_command(label="Save",command=save_file,accelerator="Ctrl+S")
mb.add_command(label="Save as..",command=save_as,accelerator="Ctrl+Shift+S")
mb.add_separator()
# mb.add_command(label="Page Setup")
# mb.add_command(label="Print",accelerator="Ctrl+P")
# mb.add_separator()
mb.add_command(label="Exit                                    ",accelerator="F2",command=exit)
em = Menu(menu,tearoff=False)
menu.add_cascade(label="Edit",menu=em)
em.add_cascade(label="Undo        Ctrl+Z",command=txtarea.edit_undo)
# em.add_cascade(label="Redo        Ctrl+R",command=txtarea.edit_redo)
em.add_separator()
em.add_cascade(label="Cut        Ctrl+X",command=cut)
em.add_cascade(label="Copy        Ctrl+C",command=copy)
em.add_cascade(label="Paste        Ctrl+V",command=paste)
em.add_cascade(label="Delete        Del",command=delete)
em.add_separator()
em.add_cascade(label="Search with google        Ctrl+E",command=search)
# em.add_cascade(label="Find..        Ctrl+F")
# em.add_cascade(label="Find Next        F3")
# em.add_cascade(label="Find Previous        Shift+F3")
# em.add_cascade(label="Replace        Ctrl+H")
# em.add_cascade(label="Go To..        Ctrl+G")
em.add_separator()
em.add_cascade(label="Select All..        Ctrl+A",command=sel)
em.add_cascade(label="Time/Date        F5",command=td)
fr = Menu(menu,tearoff=False)
menu.add_cascade(label="Format",menu=fr)
ch = IntVar()
fr.add_checkbutton(label="Wrap",command=wr,variable=ch,onvalue=1,offvalue=0)
fr.add_cascade(label="Font..",command=fnt)
fr.add_cascade(label="Background Color",command=bgcolor)
fr.add_cascade(label="Foreground Color",command=fgcolor)
zoom = Menu(tearoff=False)
zoom.add_cascade(label="Zoom In     Ctrl+=",command=inc)
zoom.add_cascade(label="Zoom Out     Ctrl+D",command=dec)
zoom.add_cascade(label="Restore Default Zoom     Ctrl+0",command=df)
view = Menu(menu,tearoff=False)
menu.add_cascade(label="View",menu=view)
view.add_cascade(label="Zoom",menu=zoom)
# view.add_checkbutton(label="Status Bar")
hlp = Menu(menu,tearoff=False)
menu.add_cascade(label="Help",menu=hlp)
hlp.add_cascade(label="View Help",command=help_me)
# hlp.add_cascade(label="Send Feedback")
hlp.add_separator()
hlp.add_cascade(label="About Notepad",command=about)
window.mainloop()