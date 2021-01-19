from . import speakandlisten
import datetime
import json

def reminder():
    
    tp = (print("What's the Title?"), speakandlisten.speak("What's the Title?"))
    #getting the title
    t = input()

    mp = (print("What's the Message?"), speakandlisten.speak("What's the Message?"))
    #getting the message
    m = input()
    
    

    #capitalizing the first word
    t.capitalize()
    m.capitalize()

    #getting current datetime for example
    d = (datetime.datetime.now().strftime("%I:%M %p"))
    tm = (datetime.datetime.now().strftime("%d-%m-%Y"))
    dt = (d + ' ' + tm)
    print(dt)

    #taking the datetime inout from the user
    time = input("Enter the time in the given format")
    date = input("Enter the date in the given format")

    d_t = (time + " " + date)
    print("You'll be reminded at " + d_t)
    speakandlisten.speak("You'll be reminded at " + d_t)

    reminder_data = {}
    reminder_data["time"]  = time
    reminder_data["date"] = date
    reminder_data["title"] = t
    reminder_data["message"] = m

    with open("rem" + ".json", "w+") as r:
        json.dump(reminder_data, r)
