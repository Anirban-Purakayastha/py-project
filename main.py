import speech_recognition as sr
import pyttsx3
import webbrowser
from openai import OpenAI

recognizer = sr.Recognizer()
engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
   
    client = OpenAI(api_key="sk-R6FQigFxW09V-IzypjEURQv7GEvaCxSa1m7lEDwWVeT3BlbkFJSWkLpxol_fyw9aUhXW0KQja_RFtcaqWCd3VTj8-ewA")

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant."},
        {
            "role": "user",
            "content": command
        }
    ]
    )

    return (completion.choices[0].message)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    
    else:
        output= aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing jarvis...")
    #listen the wake word to initialize jarvis
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()
       
        print("recognizing......") 
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = r.listen(source)
                    command= r.recognize_gooogle(audio)
                    processCommand(command)

        
        
        except Exception as e:
            print("error; {0}".format(e))