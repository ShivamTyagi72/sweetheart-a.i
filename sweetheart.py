import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

print(" -------------------------WELCOME TO SWEETHEART A AI DESKTOP ASISTANT---------------------")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#speak function will speak the function passed to it


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


print("initializing sweetheart...")
speak("initializing sweetheart...")



#this function will wish you as per current time


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am sweetheart Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        speak(" say that again please ...") 
        query=None
        return "None"
    return query



wishMe()

query=takeCommand()
  # Logic for executing tasks based on query
if 'wikipedia' in query.lower():
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

elif 'open youtube' in query.lower():
            #webbrowser.open("youtube.com")

 url="youtube.com"
 chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
 speak(" opening youtube for you...")

 webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
            #webbrowser.open("google.com")

 url="google.com"
 chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
  
 speak(" opening google for you...")
 webbrowser.get(chrome_path).open(url)

elif 'twitter' in query.lower():
            #webbrowser.open("twitter.com")   


 url="twitter.com"
 chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
 speak(" opening twitter for you...")
 webbrowser.get(chrome_path).open(url)


elif 'instagram' in query.lower():
            #webbrowser.open("twitter.com")   


 url="instagram.com"
 chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
 speak(" opening instagram for you...")
 webbrowser.get(chrome_path).open(url)



elif 'facebook' in query.lower():
            #webbrowser.open("twitter.com")   


 url="facebook.com"
 chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
 speak(" opening facebook for you...")
 webbrowser.get(chrome_path).open(url)



 


elif 'play music' in query.lower():
         music_dir = 'D:\cvm\songs'
         songs = os.listdir(music_dir)
         print(songs)
         speak("playing music for you....")   
         speak("playing music for you ...") 
         os.startfile(os.path.join(music_dir, songs[0]))

elif ' time' in query.lower():
         strTime = datetime.datetime.now().strftime("%H:%M:%S")  
         print(strTime)  
         speak(f"sir, the time is {strTime}")

elif 'open code' in query.lower():
         speak(" opening the code of sweetheart for you..")
         codePath = "C:\\Users\\tyagi\\Desktop\\SWEETHEART\\sweetheart.py"
         
         os.startfile(codePath)





        