import datetime

def get_time():
    #grtting the time
    return  datetime.datetime.now().strftime("%I:%M %p")