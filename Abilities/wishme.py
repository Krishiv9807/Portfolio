import datetime
from . import speakandlisten

def wishMe():
    #getting the time
    hour = int(datetime.datetime.now().hour)
    
    #checking that the time is between 4am and 12pm
    if hour >= 4 and hour <= 12:
        speakandlisten.speak("Good Morning Boss!")
    
    #checking that the time is between 12pm and 4pm
    elif hour >= 12 and hour <16:
        speakandlisten.speak("Good Afternoon Boss!")
    
    #telling the function to say Good Evening at other time
    else:
        speakandlisten.speak("Good Evening Boss!")
    
    speakandlisten.speak("How can I help you?")