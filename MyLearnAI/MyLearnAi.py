#First we write the speak function so that the A.I. can say something
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import smtplib #This module is used for sending mail to any machine by defining an SMTP client 
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
#In the above line we write 0 for male voice and 1 for female voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("Welcome to MyLearnAI. Please tell me how may I help you?")

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

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('Youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com')
#     server.close()

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
        #basic codes that I wrote while learning about the webbrowser module
        #These codes open basic simple websites a user would want the A.I. to open
        # elif 'open youtube' in query:
        #     webbrowser.open("youtube.com")
        
        # elif 'open google' in query:
        #     webbrowser.open("google.com")
        
        # elif 'open stackoverflow' in query:
        #     webbrowser.open("stackoverflow.com")
            
        # elif 'play music' in query:
        #     music_dir = 'D:\\MyMusic'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[1]))
            
        elif 'the time' in query:
            #The function to make the A.I. tell us the time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Yes sir, the time is {strTime}")
            print(strTime)
            
        elif 'open code' in query:
            #The function to open vs code if the user wants to edit the source code
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        
        elif 'email to vivek' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ruchiryouremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            
            except Exception as e:
                print(e)
                speak("Sorry sir the email cannot be sent")
                
        elif 'open my website' in query:
            # directory_path = "D:\\CS Project Website"
            # file_name = "index.html"
            # file_path = os.path.join(directory_path, file_name)
            # try:
            #     with open(file_path, 'r') as file:
            #         content = file.read()
            #         print(content)
            # except FileNotFoundError:
            #     speak("Sorry sir,File not found.")
            # except Exception as e:
            #     speak(f"Error occurred: {e}")
            file_path = r"D:\CS Project Website\index.html" #locates my html file
            webbrowser.open("file://" + file_path, new=2) #opens my html file in a new tab
            #I can change it to open in new window by changing th evalue of new to 1
            speak("Reopening vs code to take further query")
            code_path = r"C:\Users\user\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            subprocess.Popen([code_path, '--reuse-window']) #The subprocess module opens vs code again in the last 
                                                            #closed part so that we can give further commands 
            query2 = takeCommand().lower()
            if 'open personalized learning paths' in query2:
                #For now I have added link of the development server but I will change it once we host the site properly
                webbrowser.open("http://127.0.0.1:5500/Personalized%20Learning%20Paths.html")
            else:
                speak("Webpage not available")



