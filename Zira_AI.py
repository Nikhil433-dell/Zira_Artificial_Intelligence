from ssl import SSLContext
import pyttsx3  # for importing engine
import datetime # for time
import speech_recognition as sr # for recognitizing audio from google
import wikipedia # for taking information from wikipedia
import os # for opening browser and softwares
import webbrowser
import random # for generating random number for playing random music
import pyautogui
# import pocketsphinx
from playsound import playsound
from googlesearch import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
# print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    # function for speaking to AI
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    # for wishing user according to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        # speak('Good Morning!')
        speak('Good Morning!')

    elif hour>=12 and hour<3:
        speak('Good Afternoon!')
        # speak('Good Afternoon!')

    else:
        speak('Good Evening!')
        # speak('Good Evening!')

    speak(' I am Zira, Your Virtual assistant. How can I help you?')
    
    
def takeCommand():
    # Use microphone for taking input value and recognize it in string value
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        r.energy_threshold = 1171.3662241235445
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(Exception)
        print("Say that again please...")
        return "None"
    return query

def hit(key):
    pyautogui.keyDown(key)
    return


# def new_func(r, source):
#     audio = r.listen(source)
#     return audio


if __name__=='__main__':
    # speak("Hello, my self Zira. I am written in python programming language and my maker is Nikhil ")
    speak("tell me the password")
    passwrd = takeCommand().lower()
    if "programmer" in passwrd: 
        try:
            playsound('C:\\Users\\Prashansha\\Desktop\\my songs\\my favourites\\Windows 11 start sound YTECHB.mp3')
        except Exception as e:
            print(e)
        # speak(f"password is correct")
        speak("welcome Prasansha")
        wishMe() 
        # speak("I can do upto ten functions")
        while True:

            query = takeCommand().lower()
                

            if "change the owner" in query: # for changing owner, working properly
                speak("the owner is nikhil. if you want to change the owner")
                speak("tell me the new owner name")
                owner = takeCommand().lower()
                speak(f"Ok, owner setted to {owner}")

            elif "introduce yourself" in query:
                speak("Hello, my self Zira. I am written in python programming language and my maker is Nikhil ")

            elif "how are you" in query:
                speak("i am fine, give me commands!")

            elif "your name" in query:
                speak(f"I am zira and my owner is {owner}")


            elif 'wikipedia' in query:  # for searching from wikipedia working properly
                speak('Searching Wikipedia...')
                query = query.replace('wikipedia','')
                results = wikipedia.summary(query,sentences=2)
                print(results)
                speak(results)

            elif "open youtube" in query: # working properly
                speak("opening youtube")
                webbrowser.open("https://youtube.com")

            elif "open instagram" in query:  # working properly
                speak("opening instagram")
                webbrowser.open("https://instagram.com")

            elif "search" in query:  # working properly
                speak("what you want to search in browser")
                query = takeCommand().lower()
                #iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
                chrome_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
                for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                    webbrowser.open("https://google.com/search?q=%s" % query)

            elif "open facebook" in query:  # working properly
                speak("opening facebook")
                webbrowser.open("https://facebook.com")

            elif "open stack overflow" in query: 
                speak("opening stack overflow")
                webbrowser.open("https://stackoverflow.com")

            elif "switch off" in query:
                speak("ok, exiting the programme")
                exit()

            elif "close the programm" in query:
                speak("ok, exiting the programme")
                exit()
                

            elif "play music" in query:  # for playing random music from favourite directory
                music_dir = 'C:\\Users\\Prashansha\\Desktop\\my songs\\my favourites'
                songs = os.listdir(music_dir)
                randno = random.randint(1,60)
                os.startfile(os.path.join(music_dir,songs[randno]))
                speak(f"Song number {randno} is playing!")
                print(f"Song number {randno} is playing!")

            elif "play some music" in query:  # for playing random music from favourite directory
                music_dir = 'C:\\Users\\Prashansha\\Desktop\\my songs\\my favourites'
                songs = os.listdir(music_dir)
                randno = random.randint(1,28)
                os.startfile(os.path.join(music_dir,songs[randno]))
                speak(f"Song number {randno} is playing!")
                print(f"Song number {randno} is playing!")

            elif "the time" in query:  # for telling time, working properly
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"the time is {strtime}")
                speak(f"the time is {strtime}")

            elif "open vs code" in query:  # working properly
                vspath = "C:\\Users\\Prashansha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
                os.startfile(vspath)
                speak('opening visual studio code')

            elif "open google" in query:  # working properly
                cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
                os.startfile(cpath)
                speak('opening google chrome')

            elif "open browser" in query:  # working properly
                cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
                os.startfile(cpath)
                speak('opening google chrome')

            elif "switch off" in query:
                speak("ok, closing the program")
                print("ok, closing the program")
                exit()

            else:
                speak("say that again please")
                speak("this is not in my command functions")

    else:
        speak('wrong password')


        
                
                

        