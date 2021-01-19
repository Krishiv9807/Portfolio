from . import set_reminder
import datetime
from plyer import notification
from . import speakandlisten
import json

notification_icon = r'C:\Users\HP\Desktop\krishiv\Assistant\Abilities\notification.ico'

with open('rem' + '.json', 'r') as r:
    cr = json.load(r)

while True:
        #checking if the time of the datime input is equal to current time
        if datetime.datetime.now().strftime("%I:%M %p") == cr['time']:
            #checking if the date of the datetime input in equal to currrent datetime
            if datetime.datetime.now().strftime("%d-%m-%Y") == cr['date']:
                speakandlisten.speak(set_reminder.m)
                notification.notify(
                    
                    #defining title as t
                    title = cr['title'],    
                    #defining message as m
                    message = cr['message'],
                    #defining the notification icon
                    app_icon = notification_icon,
                    #seting the timeout
                    timeout=10
                
                )
            else:
                print("Try Again")
            break