import pyjokes
from . import speakandlisten

def joke():
    #getting jokes in variabe j
    j = pyjokes.get_joke()
    print(j)
    speakandlisten.speak(j)