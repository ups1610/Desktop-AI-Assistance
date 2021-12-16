import audioop
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
controlfreq=180
engine.setProperty('rate',controlfreq)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime('%I:%M:%S')
    speak('the current time is')
    speak(Time)    

def date():
    year=int(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak('The current date is')
    speak(date)
    speak(month)
    speak(year)

def task():
    speak('Welcome back sir! Hope you are well')
    hour = datetime.datetime.now().hour

    if hour>=6 and hour <12:
        speak('Good Morning')
    elif hour>=12 and hour <18:
        speak('Good Afternoon')
    elif hour>=18 and hour<24:
        speak('Good Evening')
    else:
        speak('Good Night')

    speak('Jaarvis at your service. How can I help you') 

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source)

    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(query)    
    except Exception as e:
        print(e)
        speak('Say that again please...')

        return 'None'    
    return query
def sendmail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.echlo()
    server.starttls()
    server.login('pratapsinghupendra96@gmail.com','123test')
        

if __name__ == "__main__":
    
    task()

    while True:
        query=takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif"offline"  in query:
            speak("Jarvis happy to serve!.Come back again Thank you")
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            speak(result)
        elif "open chrome" in query:
            speak('opening....')
            speak('what I would search')
            chromepath="C:\Program Files\Google\Chrome\Application\chrome.exe %s" 
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ ".com")





    
