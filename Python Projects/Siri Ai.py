import datetime
import os
import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good mornig sir ji")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir ji")
    else:
        speak("good evening sir ji")
    speak('i am Jarvis. how can i help you sir ji')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognissing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        # print(e)
        print("say that again please")
        return 'none'
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak('seraching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play' in query:
            song=query.replace('play','')
            speak(song)
            pywhatkit.playonyt(song)
        elif 'open code' in query:
            path = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'quite' in query:
            exit
