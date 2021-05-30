import os
from tkinter.filedialog import askdirectory
from tkinter import *
import pygame
root = Tk()
root.minsize(300,300)
root.title("MUSIC PLAYER")
root.iconbitmap("music.ico")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry("1300x800+200+10")
list = []
flag = False
index = 0
stp = StringVar()
stp.set("PAUSE")
def next_song():
    global index
    try:
        if len(list) == 1:
            pygame.mixer.music.load(list[0])
            track.set(list[0])
            pygame.mixer.music.play()
            status.set("--PLAYING")
        else:
            index += 1
            pygame.mixer.music.load(list[index])
            track.set(list[index])
            pygame.mixer.music.play()
            status.set("--PLAYING")
    except:
        pass
def pre_song():
    global index
    try:
        if len(list) == 1:
            pygame.mixer.music.load(list[0])
            track.set(list[0])
            pygame.mixer.music.play()
            status.set("--PLAYING")
        else:
            index -= 1
            pygame.mixer.music.load(list[index])
            track.set(list[index])
            pygame.mixer.music.play()
            status.set("--PLAYING")
    except:
        pass
def stop_song():
    try:
        pygame.mixer.music.stop()
        status.set("--STOPPED")
    except:
        pass
Paused = False
    # Declaring track Variable
track = StringVar()
    # Declaring Status Variable
status = StringVar()
index = 0
flag = False
def play_song():
    global flag
    try:
    # Displaying Selected Song title
        track.set(playlist.get(ACTIVE))
    # Displaying Status
        if flag:
            status.set("--PLAYING")
        else:
            pass
    # Loading Selected Song
        pygame.mixer.music.load(playlist.get(ACTIVE))
    # Playing Selected Song
        pygame.mixer.music.play()
    except:
        pass
def toggle():
    try:
        global Paused
        if Paused:
            unpause_song()
            stp.set("PAUSE")
            Paused = False
        else:
            pause_song()
            stp.set("RESUME")
            Paused = True
    except:
        pass
def pause_song():
    global flag
    try:
        if flag:
    # Displaying Status
            status.set("--PAUSED")
        else:
            pass
    # Paused Song
        pygame.mixer.music.pause()
    except:
        pass
def unpause_song():
    global flag
    try:
        if flag:
    # Displaying Status
            status.set("--PLAYING")
        else:
            pass
    # Playing back Song
        pygame.mixer.music.unpause()
    except:
        pass
#adding song from directory.
def add_song():
    global flag
    try:
        directory = askdirectory()
        os.chdir(directory)
        for files in os.listdir(directory):
            if files.endswith(".mp3"):
                playlist.insert(END,files)
                list.append(files)
                flag = True
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0)
    except:
        pass
#set volume.
def control_volume(vol):
    try:
        frequency = int(vol) / 100
        pygame.mixer.music.set_volume(frequency)
    except:
        pass
    # Creating Track Frame for Song label & status label
trackframe = LabelFrame(root,text="SONG STATUS",font=("times new roman",15,"bold"),bg="grey",fg="lime",bd=5,relief=GROOVE)
trackframe.place(x=0,y=0,width=w,height=300)
    # Inserting Song Track Label
songtrack = Label(trackframe,textvariable=track,width=30,font=("times new roman",24,"bold"),bg="grey",fg="blue").grid(row=1,column=0,padx=150,pady=100)
    # Inserting Status Label
trackstatus = Label(trackframe,textvariable=status,font=("times new roman",24,"bold"),bg="grey",fg="blue").grid(row=1,column=1,padx=10,pady=100)

    # Creating Button Frame
buttonframe = LabelFrame(root,text="CONTROL",font=("times new roman",15,"bold"),bg="grey",fg="lime",bd=5,relief=GROOVE)
buttonframe.place(x=0,y=300,width=w,height=300)
play = Button(buttonframe,bd=5,text="PLAY",command=play_song,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold",activebackground="red",activeforeground="pink").grid(row=1,column=0,padx=25,pady=120)
pause = Button(buttonframe,bd=5,textvariable=stp,command=toggle,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold",activebackground="red",activeforeground="pink").grid(row=1,column=1,padx=25,pady=120)
    # Inserting Stop Button
stop = Button(buttonframe,bd=5,text="STOP",command=stop_song,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold",activebackground="red",activeforeground="green").grid(row=1,column=2,padx=25,pady=120)
    #Add song
add_song = Button(buttonframe,bd=5,text="ADD SONG",command=add_song,width=9,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold",activebackground="red",activeforeground="pink").grid(row=1,column=3,padx=25,pady=120)
next = Button(buttonframe,bd=5,text="NEXT",command=next_song,width=7,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold",activebackground="red",activeforeground="pink").grid(row=1,column=5,padx=25,pady=120)
previous = Button(buttonframe,bd=5,command=pre_song,text="Previous",width=7,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold",activebackground="red",activeforeground="pink").grid(row=1,column=4,padx=25,pady=120)
    # Creating Playlist Frame
songsframe = LabelFrame(root,text="PLAYLIST",font=("times new roman",15,"bold"),bg="grey",fg="lime",bd=5,relief=GROOVE)
songsframe.place(x=0,y=600,width=w,height=300)
    # Inserting scrollbar
scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    # Inserting Playlist listbox
playlist = Listbox(songsframe,selectmode=SINGLE,yscrollcommand=scrol_y.set,font=("times new roman",12,"bold"),bg="silver",fg="black",bd=5,relief=GROOVE)
    # Applying Scrollbar to listbox
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)
#volume scale
scale = Scale(buttonframe,from_=0,to=100,orient=VERTICAL,command=control_volume,cursor="arrow",length=200,activebackground="blue",bg="tomato",font=("helvatica",20,"italic"),bd=4,fg="lime",highlightbackground="yellow",highlightcolor="black",relief=GROOVE,sliderlength=25).grid(row=1,column=7,padx=15)
#volume label
volume_lable = Label(buttonframe,text="Volume Control : ",width=15,height=2,font=("times new roman",16,"bold"),fg="blue",bg="gray",activebackground="red",activeforeground="pink").grid(row=1,column=6,padx=25)
root.mainloop()