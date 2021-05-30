from tkinter import *
exp = ''
def click(item):
    global exp
    exp = exp+str(item)
    txt.set(exp)
def clear():
    global exp
    txt.set(" ")
    exp = " "
def eval_exp():
    global exp
    try:
        x = eval(txt.get())
        txt.set(x)
        exp = " "
    except Exception as ex:
        txt.set('Error!')
        exp = " "
def back():
    r = txt.get()
    global exp
    if r == 'Error!':
        txt.set(" ")
        exp = " "
    elif len(r) != 0:
        txt.set(r[:-1])
        exp = " "
    else:
        exp = " "
        txt.set(" ")
root = Tk()
root.title("Calculator")
root.geometry("590x345+500+250")
root.config(background="skyblue")
root.iconbitmap("calculator.ico")
root.resizable(0,0)
txt = StringVar()
input_box=Entry(root,text=txt,fg="red",bg="lime",font=("times new roman",20,"bold"),relief=RAISED).pack(fill=X,anchor='center')
btn_frame = Frame(root,height=500,bg='lime',width=600).place(y=38)
btn = Button(btn_frame,text='7',command=lambda:click(7),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=15,y=55)
btn = Button(btn_frame,text='8',command=lambda:click(8),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=110,y=55)
btn = Button(btn_frame,text='9',command=lambda:click(9),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=210,y=55)
btn = Button(btn_frame,text='4',command=lambda:click(4),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=310,y=55)
btn = Button(btn_frame,text='5',command=lambda:click(5),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=410,y=55)
btn = Button(btn_frame,text='6',command=lambda:click(6),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=510,y=55)
btn = Button(btn_frame,text='1',command=lambda:click(1),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=15,y=130)
btn = Button(btn_frame,text='2',command=lambda:click(2),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=110,y=130)
btn = Button(btn_frame,text='3',command=lambda:click(3),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=210,y=130)
btn = Button(btn_frame,text='%',command=lambda:click('%'),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=310,y=130)
btn = Button(btn_frame,text='0',command=lambda:click(0),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=410,y=130)
btn = Button(btn_frame,text='.',command=lambda:click('.'),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=510,y=130)
btn = Button(btn_frame,text='/',command=lambda:click('/'),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=15,y=210)
btn = Button(btn_frame,text='+',command=lambda:click('+'),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=110,y=210)
btn = Button(btn_frame,text='-',command=lambda:click('-'),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=210,y=210)
btn = Button(btn_frame,text='*',command=lambda:click('*'),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=310,y=210)
btn = Button(btn_frame,text='AC',command=lambda:clear(),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=410,y=210)
btn = Button(btn_frame,text='CUT',command=lambda:back(),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=4).place(x=510,y=210)
btn = Button(btn_frame,text='=',command=lambda:eval_exp(),font=('times new roman',15,'bold'),relief=GROOVE,bd=5,width=45).place(x=15,y=285)
root.mainloop()