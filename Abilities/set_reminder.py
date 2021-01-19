from plyer import notification
from . import speakandlisten
import datetime

def reminder():
    
    tp = (print("What's the Title?"), speakandlisten.speak("What's the Title?"))
    #getting the title
    t = input()

    mp = (print("What's the Message?"), speakandlisten.speak("What's the Message?"))
    #getting the message
    m = input()
    
    notification_icon = r'C:\Users\HP\Desktop\krishiv\Assistant\Abilities\notification.ico'

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


    while True:
        #checking if the time of the datime input is equal to current time
        if datetime.datetime.now().strftime("%I:%M %p") == time:
            #checking if the date of the datetime input in equal to currrent datetime
            if datetime.datetime.now().strftime("%d-%m-%Y") == date:
                speakandlisten.speak(m)
                notification.notify(
                    
                    #defining title as t
                    title = t,    
                    #defining message as m
                    message = m,
                    #defining the notification icon
                    app_icon = notification_icon,
                    #seting the timeout
                    timeout=10
                
                )
            else:
                print("Try Again")
            break
