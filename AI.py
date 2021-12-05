from time import time
import subprocess
import wolframalpha
import tkinter
import json
import operator
import winshell
import smtplib
import feedparser
import pyttsx3
import ctypes
import requests
import speech_recognition as sr
import datetime
import os
import webbrowser
import random
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wc
from urllib.request import urlopen
from requests import *
import wikipedia
import pywhatkit
import smtplib
import sys
import pyjokes
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import instaloader
import PyPDF2
engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
listener = sr.Recognizer()
#for speaking purpose.
def speak(audio):
    # print(audio)
    engine.say(audio)
    engine.runAndWait()
#for taking user command.
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening to you...')
            listener.pause_threshold=5
            audio = listener.listen(source,phrase_time_limit=3,timeout=8)
            try:
                print('Recognizing...')
                query = listener.recognize_google(audio,language='en-in')
                print(f"You said : {query}\n")
            except Exception as ex:
                speak("say that again please")
                return "None"
            return query
    except:
        speak("Input device unavailabel!")
#for whishing me.
def wish_me():
    speak("Hello Master!")
    hour = int(datetime.datetime.now().hour)
    x = ""
    if hour >= 0 and hour < 12:
        speak("Good Morning.")
        x = "AM"
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon.")
        x = "PM"
    else:
        speak("Good Evening.")
        x = "PM"
    H = datetime.datetime.now().hour
    M = datetime.datetime.now().minute
    S = datetime.datetime.now().second
    speak(f"it's {H}:{M}:{S} {x}.Jarvis is here,how can i help you?")
#sending email to chandni.
def sendEmail(to,content):
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("rahmatullahansari38@gmail.com","Rahmat786.ra")
        server.sendmail("rahmatullahansari38@gmail.com",to,content)
        server.close()
    except Exception as ex:
        speak("connection error,sorry!")
#what i can do
def stop_what_can_i_do():
    with sr.Microphone() as src:
        listener.pause_threshold = 1
        sound = listener.listen(src,phrase_time_limit=3,timeout=5)
        query = ""
        try:
            query = listener.recognize_google(sound,language='en-in')
            print(f"{query}")
        except Exception as ex:
            pass
        return query
#fetching news
def news():
    try:
        url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-11-19&sortBy=publishedAt&apiKey=acd6413464ce4883a10ee9239394eb71"
        page = requests.get(url).json()
        articles = page["articles"]
        headline = []
        day = ["first","second","third","fourth","fifth"]
        for article in articles:
            headline.append(article["title"])
        for i in range(len(day)):
            speak(f"Today's {day[i]} news is {headline[i]}")
    except Exception as ex:
        speak("connection error,sorry!")
#tweeter.
def twitter(t):
    try:
        email = 'rahmatullaha845@gmail.com'
        password = 'Rahmat786.ra'
        twit =  t
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get("https://twitter.com/login")
        expath = '//t*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
        pxpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
        login = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div'
        time.sleep(2)
        driver.find_element_by_xpath(expath).send_keys(email)
        time.sleep(0.5)
        driver.find_element_by_xpath(pxpath).send_keys(password)
        time.sleep(0.5)
        driver.find_element_by_xpath(login).click()
        tweetxpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg'
        messagexpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        postxpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'
        time.sleep(4)
        driver.find_element_by_xpath(tweetxpath).click()
        time.sleep(0.5)
        driver.find_element_by_xpath(messagexpath).send_keys(twit)
        time.sleep(0.5)
        driver.find_element_by_xpath(postxpath).click()
    except Exception as ex:
        speak("something went wrong sorry!")
#read pdf
def read_pdf():
    pth = 'E:\\Python.pdf'
    #pdfs = os.listdir(pth)
    #pdflist = []
    #for i in pdfs:
        #if i.endswith(".pdf"):
            #pdflist.append(i)
        #else:
            #pass
    #pdf = random.choice(pdflist)
    speak(f"i am going to read {pth} file")
    #book = open(f'{pdf}','rb')
    pdf_reader = PyPDF2.PdfFileReader(pth)
    pages = pdf_reader.numPages
    speak(f"Total number of pages in this book is {pages}")
    page = pdf_reader.getPage(5)
    text = page.extractText()
    speak(text)
    speak("task complete sir,I am ready for next command.")
#main function start from here.
if __name__ == "__main__":
    clear = lambda:os.system('cls')
    clear()
    wish_me()
    what_i_can_do =["open and close notepad","open and close VS code",
    "open and close IntelliJ idea","open and close android studio",
    "open and close command prompt",
    "shutdown and restart your system","open google",
    "open youtube","play music on youtube","play music",
    "open youtube","tell your IP address",
    "read wikipedia from internet",
    "send email","open facebook","open instagram",
    "tell jokes","switch window","speak news","open twitter and can twit",
    "tell your location","take screenshot",
    "download instagram profile picture","read PDF",
    "hide file and folder","lock window","clean recycle bin"]
    fine = False
    while True:
        try:
            query = take_command().lower()
            if "open notepad" in query or "notepad" in query:
                os.startfile("C:\\Windows\\System32\\notepad.exe")
            elif "close notepad" in query or "close note" in query:
                os.system('taskkill /f /im notepad.exe')
            elif "open code" in query or "code" in query or "open vs code" in query:
                os.startfile("C:\\Users\\rahma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                code = True
            elif "close code" in query or "close vs code" in query:
                os.system('taskkill /f /im Code.exe')
            elif "open idea" in query or "idea" in query or "open IntelliJ idea" in query:
                os.startfile("C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.4\\bin\\idea64.exe")
                intelli = True
            elif "close idea" in query or "close IntelliJ idea" in query:
                os.system("taskkill /f /im idea64.exe")
            elif "studio" in query or "open studio" in query or "open android studio" in query:
                os.startfile("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe")
                std = True
            elif "close studio" in query or "close android studio" in query:
                os.system("taskkill /f /im studio64.exe")
            elif "shutdown" in query or "switch off system" in query:
                speak("do you want to shut down your system?")
                take = take_command()
                if take == "yes" or take == "shutdown":
                    print("Shutting down.....")
                    os.system("shutdown /s /t 10") 
                else:
                    pass
            elif "open command prompt" in query or "command" in query or "open cmd" in query:
                os.system("start cmd")
            elif "close command prompt" in query or "close cmd" in query:
                os.system("taskkill /f /im cmd.exe")
            elif "open google" in query or "google" in query:
                speak("what you want to search?")
                cm = take_command()
                try:
                    if cm != "nothing" or cm != "just open" or cm != "None":
                        webbrowser.open(f"{cm}")
                    else:
                        webbrowser.open("www.google.com")
                except Exception as ex:
                    speak("connection error,sorry!")
            elif "song" in query or "music" in query or "play music" in query:
                try:
                    pth = "F:\\Qawwali"
                    songs = os.listdir(pth)
                    os.startfile(os.path.join(pth,random.choice(songs)))
                except Exception as ex:
                    speak("No song here.")
            elif "open youtube" in query or "youtube" in query:
                speak("what you want to search?")
                take = take_command().lower()
                try:
                    if take != "nothing" or take != "just open" or take != "None":
                        webbrowser.open(f"{take}")
                    else:
                        webbrowser.open("www.youtube.com")
                except Exception as ex:
                    speak("connection error,sorry!")
            elif "ip address" in query:
                try:
                    ip = get("https://api.ipify.org").text
                    speak(f"Your IP address is : {ip}\n")
                except Exception as ex:
                    speak("connection error,sorry!")
            elif "restart" in query or "restart the system" in query:
                speak("do you want to restart your system.")
                r = take_command()
                if r == "yes":
                    os.system("shutdown /r /t 10")
                else:
                    pass
            elif "sleep the system" in query or "sleep" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
            elif "wikipedia" in query:
                speak("what you want to search")
                query = take_command()
                speak("searching wikipedia...")
                speak("speaking wikipedia....")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query,sentences=5)
                speak(f"According to wikipedia,{result}\n")
            elif "play song on youtube" in query:
                speak("what you want to play?")
                cm = take_command().lower()
                try:
                    if cm != "nothing":
                        pywhatkit.playonyt(f"{cm}")
                    else:
                        pass
                except Exception as ex:
                    speak("connection error,sorry!")
            elif "send email" in query:
                try:
                    speak("what you want to send?")
                    content = take_command()
                    to = "chandnisahu27@gmail.com"
                    sendEmail(to,content)
                    speak("Email sent.")
                except Exception as ex:
                    speak("connection error,sorry!")
            elif "open facebook" in query or "facebook" in query:
                try:
                    webbrowser.open("www.facebook.com")
                except Exception as ex:
                    speak("connection error,sorry!")
            elif "open instagram" in query or "instagram" in query:
                try:
                    webbrowser.open("www.instagram.com")
                except Exception as ex:
                    speak("connection error,sorry!")
            elif "tell me a joke" in query:
                try:
                    jk = pyjokes.get_joke()
                    speak(jk)
                except Exception as ex:
                    speak("connection error,sorry!")
            elif "what you can do" in query:
                speak("let me check what can i do.")
                for i in what_i_can_do:
                    speak(f"I can {i}")
                    take = stop_what_can_i_do()
                    if take == "ok fine" or take == "ok":
                        break
                    else:
                        continue
            elif "switch window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            elif "tell me news" in query or "tell news" in query or "news" in query:
                speak("please wait sir,I am fetching the latest news....")
                news()
            elif "twitter" in query or "open twitter" in query:
                speak("what you want to tweet")
                twit = take_command().lower()
                twitter(twit)
            elif "location" in query or "where we are" in query:
                speak("wait sir,let me find out where we are.")
                try:
                    ip_address = get("https://api.ipify.org").text
                    print(ip_address)
                    url = 'https://get.geojs.io/vl/ip/geo/'+ip_address+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    print(geo_data)
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"Sir i am not sure ,but i think i am in {city} city of {country} country")
                except Exception as ex:
                    speak("sorry,it's network issue.")
            elif "check instagram" in query or "read instagram" in query or "instagram profile" in query:
                try:
                    speak("wait a second,i am on the way")
                    name ="code_ninja786"
                    webbrowser.open(f"www.instagram.com/{name}")
                    speak(f"{name} profile picture are find here.")
                    time.sleep(5)
                    speak("would you like to download profile picture?")
                    condition = take_command().lower()
                    if "yes" in condition or "ya" in condition:
                        mod = instaloader.Instaloader()
                        mod.download_profile(name,profile_pic_only=True)
                        speak("task complete sir,now i am ready for next command.")
                    else:
                        pass
                except Exception as ex:
                    speak("connection error,sorry!")
            elif "take screenshot" in query or "screenshot" in query or "take a screenshot" in query:
                speak("would you like to give a name to this screenshot")
                sc = take_command().lower()
                if "yes" in sc:
                    speak("please tell a name")
                    name = take_command().lower()
                    speak("wait sir i am taking screenshot.")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("task complete sir,I am ready for next command.")
                else:
                    speak("wait sir i am taking screenshot.")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save("screenshot.png")
                    speak("task complete sir,I am ready for next command.")
            #Audio book
            elif "read pdf" in query or "pdf" in query:
                read_pdf()
            elif "hide all file" in query or "hide this folder" in query or "visible for everyone" in query:
                speak("sir tell me you want to hide this folder or make it visible for everyone")
                condition = take_command().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("sir,all the files in this folder are now hidden")
                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("sir,all the files in this folder are now visible for everyone.i wish you are allowing it at your own risk")
                elif "leave it" in condition or "leave for now" in condition:
                    speak("ok sir")
                speak("task complete sir,I am ready for next command.")   
            elif "how are you" in query:
                speak("I am fine master")
                fine = True
                speak("how are you Master?")
            elif "fine" in query or "good" in query or "perfect" in query:
                if fine:
                    if "fine" in query:
                        speak("It's good to know that you are fine master.")
                    elif "good" in query:
                        speak("It's good to know that you are good master.")
                    else:
                        speak("It's good to know that you are perfect master.")
                fine = False
            elif "what's your name" in query:
                speak("I am AI assistance made by MASTER ,and called as JARVIS")
            elif "who i am" in query:
                speak("you can able to talk and ability of thinking,so definately you are HUMAN being.")
            elif 'lock window' in query or 'lock system' in query:
                speak("locking the system")
                ctypes.windll.user32.LockWorkStation()
            elif "empty recycle bin" in query or "clean recycle bin" in query or "clean recycle" in query:
                speak("cleaning recycle bin...")
                try:
                    winshell.recycle_bin().empty(confirm =False, show_progress =False,sound = True)
                except Exception as ex:
                    speak("Recycle bin is already empty.")
                speak("Task complete")
            elif "stop" in query or "dont't listen" in query:
                speak("I am going to quit for ten second")
                time.sleep(10)
            elif "write a note" in query:
                speak("what should i write?")
                mag = take_command().lower()
                speak("would you want to give a name to this note?")
                nm = take_command().lower()
                if "yes" in nm:
                    file = open(f"{nm}.txt","w")
                else:
                    file = open("Jarvis.txt","w")
                speak("would you want to include date and time?")
                st = take_command().lower()
                if st == "yes" or st == "sure":
                    H = datetime.datetime.now().hour
                    M = datetime.datetime.now().minute
                    S = datetime.datetime.now().second
                    file.write(f"{H}:{M}:{S}")
                    file.write(':=>')
                    file.write(mag)
                else:
                    file.write(mag)
            elif "show note" in query or "read note" in query:
                speak("tell me the name of note you want to read")
                nt = take_command().lower()
                file = open(f"{nt}.txt","r")
                speak(file.read())
            elif  "no thanks" in query or "sleep" in query:
                speak("thank you sir for using me,have a good day.")
                sys.exit()
        except:
            speak("Something went wrong!")