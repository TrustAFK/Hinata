import pyttsx3
import datetime
import speech_recognition 
import wikipedia
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices)
engine.setProperty("voice", voices[1].id)
rate = engine.getProperty("rate")
engine.setProperty("rate" , 135 )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<17:
        speak("good afternoon")
    elif hour>=17 and hour<19:
        speak("good evening")
    elif hour>=19 and hour<0:
        speak("good night")
    speak("hello i am hinata how may i help you")    

def take() :
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print("recognizing...")
        user_words = r.recognize_google(audio , language='en-in')
        print(user_words)
    except Exception as e:
        print(e)
        speak("can you say that again")

    return user_words       

def googling(what_to_google):
       url = "https://www.google.com.tr/search?q={}".format(what_to_google)
       webbrowser.open_new_tab(url)
    


if __name__ == '__main__':
    print("voice is active test 1 pass-----------------------------------")
    wishme()
    print("wishme pass----------------------------------")
    while True:
        user_words = take().lower()
        if "wikipedia" in user_words :
            speak("searching on wikipedia")
            text_to_search = user_words.replace("wikipedia" , "")
            print(text_to_search)
            results = wikipedia.summary(text_to_search , sentences=2)
            speak(results)
            print(results)
        elif "open youtube" in user_words:
            webbrowser.open("youtube.com")
        
        elif "open facebook" in user_words:
            webbrowser.open("facebook.com")
        
        elif "open google" in user_words:
            googling("google")

        elif "open instagram" in user_words:
               googling("instagram")
        
        elif "open fun" in user_words:
            googling("xhamster")

        elif "shut down yourself" in user_words:
            speak("ok i am shutting down sayonara")
            break    
       


    
    
