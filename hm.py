import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")



    speak("I am Friday. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)
    except Exception as e:
        #print(e)

        print("Say that again...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for wquery to do the task
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)