#First we write the speak function so that the A.I. can say something
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
#In the above line we write 0 for male voice and 1 for female voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()\

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("Hello sir my name is MyLearnAI. Please tell me how may I help you?")

def takeCommand():
    #takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    #logic for executing tasks based on query
    if 1:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak("According to wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = 'D:\\MyMusic'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'The time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Yes sir, the time is {strTime}")
            print(strTime)
            
        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            