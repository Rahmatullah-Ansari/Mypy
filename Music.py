# Importing Required Modules & libraries
from tkinter import *
import pygame
from tkinter.filedialog import askdirectory
import os
import vlc
# Defining MusicPlayer Class
class MPlayer:
    # Defining Constructor
    def __init__(self,window):
        self.window = window
        # Title of the window
        self.window.title("MUSIC PLAYER")
        # Initiating Pygame
        self.paused = False
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()
        self.w=self.window.winfo_screenwidth()
        self.h=self.window.winfo_screenheight()
        # Creating Track Frame for Song label & status label
        trackframe = LabelFrame(self.window,text="Track",font=("times new roman",15,"bold"),bg="skyblue",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=0,width=self.w-15,height=250)
        # Inserting Song Track Label
        songtrack = Label(trackframe,textvariable=self.track,width=70,font=("times new roman",24,"bold"),bg="skyblue",fg="white").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="skyblue",fg="green").grid(row=0,column=1,padx=10,pady=5)
        # Creating Button Frame
        buttonframe = LabelFrame(self.window,text="Panel",font=("times new roman",15,"bold"),bg="skyblue",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=250,width=self.w-15,height=250)
        # Inserting Play Button
        playbtn = Button(buttonframe,text="Play",command=self.songplay,width=6,height=1,font=("times new roman",16,"bold"),fg="blue",bg="skyblue",bd=5,relief=GROOVE).grid(row=0,column=1,padx=10,pady=80)
        # Inserting Pause Button
        playbtn = Button(buttonframe,text="Pause/Resume",command=self.toggle,width=12,height=1,font=("times new roman",16,"bold"),fg="blue",bg="skyblue",bd=5,relief=GROOVE).grid(row=0,column=2,padx=10,pady=80)
        #inserting a stop button.
        playbtn = Button(buttonframe,text="Stop",command=self.songstop,width=6,height=1,font=("times new roman",16,"bold"),fg="blue",bg="skyblue",bd=5,relief=GROOVE).grid(row=0,column=3,padx=10,pady=80)
        #add song button.
        playbtn = Button(buttonframe,text="Add song",command=self.addsong,width=8,height=1,font=("times new roman",16,"bold"),fg="blue",bg="skyblue",bd=5,relief=GROOVE).grid(row=0,column=4,padx=10,pady=80)
        #volume label declaration.
        scale =Scale(buttonframe,from_=0,to=100,command=self.volume,orient=HORIZONTAL,bd=5,relief=GROOVE).grid(row=0,column=6,padx=10,pady=100)
        #inserting volume text.
        vol =Label(buttonframe,text="Volume control",width=12,height=1,bd=5,relief=GROOVE,font=("times new roman",16,"bold"),fg="blue",bg="skyblue").grid(row=0,column=5,padx=10,pady=80)
        # Creating Playlist Frame
        songsframe = LabelFrame(self.window,text="Playlist",font=("times new roman",15,"bold"),bg="red",fg="white",bd=10,relief=GROOVE)
        songsframe.place(x=0,y=501,width=self.w-15,height=300)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,height=300,yscrollcommand=scrol_y.set,selectbackground="purple",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="skyblue",fg="black",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH,expand=True,side=LEFT)
        # Changing Directory for fetching Songs
    def volume(self,val):
        volume = int(val) / 100
        pygame.mixer.music.set_volume(volume)
    def addsong(self):
        directory = askdirectory()
        os.chdir(directory)
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            if track.endswith(".mp3" or ".mp4" or ".m4a"):
                self.playlist.insert(END,track)
    # Defining Play Song Function
    def songplay(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()

    def songstop(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

    def toggle(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.status.set("-playing")
            self.paused = False
        elif not self.paused:
            pygame.mixer.music.pause()
            self.status.set("-paused")
            self.paused = True
window = Tk()
window.geometry("2000x2000")
MPlayer(window)
window.mainloop()
