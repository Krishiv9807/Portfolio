import requests
from . import speakandlisten

def weather():
    speakandlisten.speak("City Name?")
    print("City Name?")
    #getting the cityname
    city = speakandlisten.takeCommand()
    #giving the apiaddress
    api_addr = "http://api.openweathermap.org/data/2.5/weather?appid=51dad51d0023f928303dc79a5945c269&q="
    #joining apiaddress and cityname to get final address
    finaladdr = api_addr+city
    print(finaladdr)
    #getting the weather results
    w = requests.get(finaladdr).json()
    #formatting the result to get only needed data
    only = (w['weather'][0]['main']), w['weather'][0]['description']
    speakandlisten.speak("The weather is")
    print("The weather is")
    print(w)
    speakandlisten.speak(only)