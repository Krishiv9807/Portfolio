from . import speakandlisten

def repeat_after_me():
    print("What to Repeat?")
    speakandlisten.speak("What to Repeat?")
    #taking the inout to speakandlisten.speak
    ltr = speakandlisten.takeCommand()
    print(ltr)
    #speaking the input
    speakandlisten.speak(ltr)