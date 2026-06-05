import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os # operating system 


engine = pyttsx3.init('sapi5')  
# ms windows gives api to get voices  # appliation programming interface
voices = engine.getProperty('voices')
# print(voices[1].id)
# print(voices)
engine.setProperty('voice', voices[0].id)
# right now we have two voices we choose first one


# it speaks whatever the string or letter passsed to it  
#run onces in main to try
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# when program runs this function runs and grett the user
def wishMe():
    hour = int(datetime.datetime.now().hour) # string value int function convert into int
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening")  

    speak(" I am Jarvis Sir. Please tell me how may I help you")       
    
    

def takeCommand():
    # uses speech recog module
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    #use microphone source
    with sr.Microphone() as source:  #microphone as source use 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # try to get audio otherwise throw exception
        print("Recognizing...") 
        # explore recg fun little bit    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        # this is jsut emppty string or non string not a function
        return "None"
    return query



if __name__ == "__main__":
    
    wishMe()
    while True:
    # if 1:
        query  = takeCommand().lower()  

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'shutdown' in query:
            break;
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open chatgpt' in query:
            webbrowser.open("https://chat.openai.com/")



        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")


        elif 'show me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

       
