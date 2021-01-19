import pyttsx3
import speech_recognition as sr

#initializing texttospeech
engine = pyttsx3.init('sapi5')      
#getting the voices available
voices = engine.getProperty('voices')
print(voices)
#setting the voice for the assistant
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #recognizing the voice input
    mv = sr.Recognizer()
    #getting mic as source of input
    with sr.Microphone() as source:
        print("Listening.....")
        mv.pause_threshold = 1
        #listning to get the input
        audio = mv.listen(source)
    try:
        #defining query in english
        query = mv.recognize_google(audio, language= 'en-in')
        print("User said : ", query) 
        return query       

    except Exception as s:
        print(s)
        
        
takeCommand()