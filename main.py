import speech_recognition as sr 
import pyttx3 
import datetime 
import webbrowser

engine = pyttx3.init()

def speak(text):
engine.say(text)
engine.runAndwait()

def listen()
recognizer = sr.recognizer()
with sr.Microphone() as source:
    print("listening...")
    audio = recognizer.listen(source)

try:
command = recognizer.recognize_google(audio).lower()
print("you said:", command)
return command
except:
    speak("sorry, I did not understand.")
    return""

    command = listen()
    if "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %P")
        speak(f"the time is {time_now}")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("open youtube")

    elif "open google" in command
    webbrowser.open("https://www.google.com")
    speak("open google")

else:
    speak("command not recognized")