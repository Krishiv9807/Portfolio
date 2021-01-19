from plyer import notification
from . import speakandlisten


def reminder():
    
    tp = (print("What's the Title?"), speakandlisten.speak("What's the Title?"))
    #getting the title
    t = speakandlisten.takeCommand()

    mp = (print("What's the Message?"), speakandlisten.speak("What's the Message?"))
    #getting the message
    m = speakandlisten.takeCommand()
    
    notification_icon = r'C:\Users\HP\Desktop\krishiv\Assistant\Abilities\notification.ico'

    #capitalizing the first word
    t.capitalize()
    m.capitalize()

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