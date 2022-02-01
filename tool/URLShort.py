from __future__ import with_statement
import contextlib
try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen
except ImportError:
	from urllib3 import urlopen
import sys
from tkinter import *;
import webbrowser
final_url=""
def show_url():
    global final_url
    url=txt.get()
    if not url=="":
        txt1.set("")
        final_url=short_url(url)
        if not final_url==None:
            txt1.set("Shorted URL = "+final_url)
    else:
        txt1.set("Empty URL,Please enter url first!")
def short_url(url):
    request_url = ('http://tinyurl.com/api-create.php?' + 
    urlencode({'url':url}))
    try:
        with contextlib.closing(urlopen(request_url)) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        txt1.set("Invalid URL")
def copy_url():
    try:
        temp=txt1.get()
        if temp.startswith("Shorted"):
            result.clipboard_clear()
            temp=temp.replace("Shorted URL = ","")
            result.clipboard_append(temp)
            txt1.set(txt1.get()+"\n\nCopied Successfully!")
        else:
            txt1.set("Please enter url and short it to copy on clip board!")
    except Exception as ex:
        pass
def open_url():
    try:
        if not final_url=="":
            webbrowser.open_new(final_url)
        else:
            txt1.set("Please enter url and short it to open!")
    except Exception as ex:
        pass
def clear_url():
    global final_url
    txt.set("")
    txt1.set("")
    final_url=""
root=Tk()
root.title("URL Shortner")
root.iconbitmap("link.ico")
root.config(bg="skyblue")
root.resizable(0,0)
label=Label(root,text="Enter URL : ")#url label.
txt=StringVar()
label.place(x=10,y=20,width=95,height=30)
entry=Entry(root,text=txt,font=("Times New Roman",14,"italic"),foreground="green")#url entry field.
entry.place(x=110,y=20,width=480,height=30)
root.geometry("600x500+250+60")
btn_short=Button(root,text="Short URL",command=show_url,foreground="blue",background="skyblue",activeforeground="blue",activebackground="skyblue")#short url.
btn_short.place(x=10,y=70,width=580,height=30)
txt1=StringVar()
result=Label(root,textvariable=txt1,font=("Times New Roman",14,"bold"))#url result.
result.place(x=10,y=120,width=580,height=200)
copy_btn=Button(root,text="Copy URL",command=copy_url,foreground="white",background="blue",activeforeground="white",activebackground="blue")#copy url button.
copy_btn.place(x=10,y=330,width=85,height=30)
open_btn=Button(root,text="Open URL",command=open_url,foreground="white",background="blue",activeforeground="white",activebackground="blue")#open url button.
open_btn.place(x=505,y=330,width=85,height=30)
clear_btn=Button(root,text="Clear",command=clear_url,foreground="white",background="blue",activeforeground="white",activebackground="blue")#open url button.
clear_btn.place(x=255,y=330,width=85,height=30)
developed_by=Label(root,text=" Developed By:\nSneha Saklani\nRitu Rajwade",font=("Times New Roman",16,"bold"),foreground="green")#developed by label.
developed_by.place(x=200,y=370,width=200,height=100)
root.mainloop()