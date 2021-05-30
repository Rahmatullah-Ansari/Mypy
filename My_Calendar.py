import calendar
from datetime import datetime
from tkinter import *
# print(calendar.month(200,6))
# print(calendar.isleap(19470))
t=0
p=False
da=False
dat=False
def select():
    global t,p,da,dat
    t = radio.get()
    print(t)
    if t == 1:
        da=True
        mnth.config(text='Enter Month:')
        p = False
        dat=False
    elif t == 2:
        dat=True
        p=False
        da=False
        s_btn.config(text='Get Date')
        mnth.config(text='Enter Day:-')
    else:
        p=True
        da=False
        dat=False
def show():
    global p,da,dat
    x=int(t1.get())
    y=int(t2.get())
    print(p)
    if p:
        c = calendar.month(x,y)
        lstbox.insert(INSERT,c)
        p = False
    elif da:
        v = calendar.weekday(x,y)
        t3.set(v)
        da = False
ttk = Tk()
ttk.title("Day or Date Finder")
ttk.geometry("700x600+300+50")
ttk.resizable(0,0)
ttk.config(bg='skyblue')
txt=StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
se = Label(ttk,text='Select option from above:',bg='skyblue',font=('times new roman',15,'bold'))
se.place(x=230,y=90,width=225,height=30)
radio = StringVar()
b = StringVar()
rd1 = Radiobutton(ttk,value=1,tristatevalue=1,variable=radio,command=select,text='Date To Day',activebackground='skyblue',bg='skyblue',font=('times new roman',15,'bold'),activeforeground='blue')
rd1.place(x=20,y=30)
rd2 = Radiobutton(ttk,value=2,tristatevalue=2,variable=radio,command=select,text='Day To Date',activebackground='skyblue',bg='skyblue',font=('times new roman',15,'bold'),activeforeground='blue')
rd2.place(x=300,y=30)
rd3 = Radiobutton(ttk,value=3,tristatevalue=3,variable=radio,command=select,text='Print Calender',activebackground='skyblue',bg='skyblue',font=('times new roman',15,'bold'),activeforeground='blue')
rd3.place(x=500,y=30)
lstbox = Text(ttk,pady=15,font=('times new roman',15,'bold'),fg='blue',wrap=CHAR)
lstbox.place(width=200,height=220,x=415,y=375)
year = Label(ttk,text='Enter Year:',bg='skyblue',font=('times new roman',15,'bold'))
year.place(x=20,y=170,width=100,height=30)
mnth = Label(ttk,text='Enter Month:',bg='skyblue',font=('times new roman',15,'bold'))
mnth.place(x=20,y=230,width=120,height=30)
e1 = Entry(ttk,textvariable=t1,bg='white',font=('times new roman',15,'bold'))
e1.place(x=220,y=170,width=300,height=30)
e2 = Entry(ttk,textvariable=t2,bg='white',font=('times new roman',15,'bold'))
e2.place(x=220,y=230,width=300,height=30)
s_btn = Button(ttk,text='Get',bg='skyblue',font=('times new roman',15,'bold'),command=show)
s_btn.place(x=300,y=280,width=150,height=50)
res = Label(ttk,text='Result:',bg='skyblue',font=('times new roman',18,'bold'))
res.place(x=20,y=430,width=100,height=30)
e3 = Entry(ttk,textvariable=t3,bg='white',font=('times new roman',15,'bold'))
e3.place(x=150,y=430,width=250,height=30)
cal = Label(ttk,text='Calendar:-',bg='skyblue',font=('times new roman',18,'bold'))
cal.place(x=500,y=340,width=120,height=30)
ttk.mainloop()