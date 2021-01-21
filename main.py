import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
import string
import requests
from plyer import notification
import pyjokes

from Abilities import speakandlisten, get_weather, get_wiki, getjoke, gettime, google_and_yt_search, playsongs, repeatafterme, set_reminder, way_wycd_info, wishme, checkrem




def main():
    
    #taking the query
    query  = speakandlisten.takeCommand()
    #checking if the query contains Google in it
    if "Google" in query:
        google_and_yt_search.google_search() 
    #checking if the query contains YouTube in it
    elif "YouTube" in query:
        google_and_yt_search.youtube_search()
    #checking if the query contains Wikipedia in it
    elif "Wikipedia" in query:
        print("What do you want to search for??")
        speakandlisten.speak("What do you want to search for??")
        get_wiki.wiki()
    #checking if the query contains joke in it
    elif "joke" in query:
        getjoke.joke()
    #checking if the query contains play songs in it
    elif "play songs" in query:
        playsongs.play_songs()
        exit()
    #checking if the query contains time in it
    elif "time" in query:
        print('getting time...')
        gettime.get_time()
        print("time is",gettime.get_time())

        speakandlisten.speak("the time is"+str(gettime.get_time()))
    #checking if the query contains weather in it
    elif "weather" in query:
        get_weather.weather()
    #checking if the query contains repeat after in it
    elif "repeat after" in query:
        repeatafterme.repeat_after_me()
    #checking if the query contains reminder in it
    elif "reminder" in query:
        set_reminder.reminder()
        checkrem.remincheck()
    #checking if the query is who are you
    elif query == "who are you":
        print ("My name is Jarvis. I am your AI Assistant")
        way_wycd_info.way_info()
    #checking if the query is what can you do for me
    elif query == "what can you do for me":
        way_wycd_info.wcyd_info()
    #checking if the query is shutdown
    elif query == "shutdown":
        hour = int(datetime.datetime.now().hour)
        #checking if the time is between 4am and 12pm
        if hour >= 4 and hour <= 12:
            speakandlisten.speak("Have a Great Day ahead Sir!")
        #checking if the time is between 12pm and 4pm
        elif hour >= 12 and hour <16:
            speakandlisten.speak("Have a Great Day ahead Sir!")
        #checking if the time is greater than 9pm
        elif hour >=21:
            speakandlisten.speak("Good Night Sir!")
        #saying the program to say good evening in other time
        else:
            speakandlisten.speak("Good Evening Sir!")
        activate_Jarvis()

    else:
        speakandlisten.speak("Sorry I couldn't quite hear what you said, can you repeat it please?")
        main()

def activate_Jarvis():
    while True:
        #taking the query
        query = speakandlisten.takeCommand()
        if query is not None:
            #checking if the query is Jarvis
            if "Jarvis" in query:
                wishme.wishMe()
                main()

main()