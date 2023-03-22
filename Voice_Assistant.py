import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import pyjokes
import os
import time
from subprocess import call

def takeCommand(user="USER"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio, language="en-in")
            print(f"\n{user} : {data}")
            return data.lower()
        except sr.UnknownValueError:
            print("Not Understanding...")
            print("Speak again...")
            return takeCommand(user)

def speak(audio):
    print(f"JARVIS : {audio}\n")
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def openPyFile(string):
    call(["python", string])

if __name__ == "__main__":
    os.system("cls")
    speak("What is your name?")
    user = takeCommand()
    user = user.upper()
    speak("Say 'Hello Jarvis' to activate the software")
    if takeCommand(user) == "hello jarvis":
        wishMe()
        while True:
            time.sleep(2)
            query = takeCommand(user)
            if "your name" in query:
                speak("My name is Jarvis")
            elif "time" in query:
                speak(datetime.datetime.now().strftime("%H:%M:%S"))
            elif "open google" in query:
                webbrowser.open("https://www.google.com/")
            elif "open youtube" in query:
                webbrowser.open("https://www.youtube.com/")
            elif "open hackerrank" in query:
                webbrowser.open("https://www.hackerrank.com/dashboard/")
            elif "open hackerearth" in query:
                webbrowser.open("https://www.hackerearth.com/challenges/")
            elif "wikipedia" in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            elif "open vs code" in query:
                vscodePath = "C:\\Users\\vishal singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(vscodePath)
            elif "open vpn" in query:
                vpnPath = "C:\\Program Files (x86)\\Proton Technologies\\ProtonVPN\\ProtonVPN.exe"
                os.startfile(vpnPath)
            elif "joke" in query:
                speak(pyjokes.get_joke(language="en", category="all"))
            elif "play song" in query:
                address = "D:\\Songs"
                listsong = os.listdir(address)
                print(listsong)
                os.startfile(os.path.join(address, listsong[0]))
            elif "repeat" in query:
                speak(takeCommand(user))
            elif "run" in query:
                speak("Which code do you want to run?")
                run_code = takeCommand(user)
                if "number" in run_code:
                    speak("Starting Phone Number.py")
                    openPyFile("Phone_Number.py")
                    break
            elif "exit" in query or "quit" in query:
                speak("I'm glad to help you. See you next time.")
                break
            else:
                speak("Sorry, I didn't get that.")
                speak("Please try anything else.")
    else:
        speak("Sorry, Jarvis signing off.")
