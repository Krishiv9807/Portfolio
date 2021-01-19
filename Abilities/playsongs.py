import webbrowser
from . import speakandlisten
import string
import os

def play_songs():
    #defining  the folder where songs are stored
    s = "H:\krish\Coding\Microsoft VS Code\Programmes\Songs"  
    #listing all the song files
    files = os.listdir(s)
    
    print("Your Choice or All?")
    speakandlisten.speak("Your Choice or All?")
    
    w = speakandlisten.takeCommand()
   
    #getting the command to play the song
    if w == ("my choice"):
        #listing all the files to the user
        print(files)
        speakandlisten.speak("Which song to play from these?")
        print("Which song to play from these?")
        #taking command for the song to play
        sp = speakandlisten.takeCommand()
        #making first letter capital of the input
        z = string.capwords(sp)
        for song in os.listdir(path=s):
            #checking if the inout matches the filename
            if song.startswith(z):
                print("playing....")
                speakandlisten.speak("playing....")
                #playing the song
                os.startfile(os.path.join(s,song))

    elif w == "all":
        #else playing the playlist containing the song files
        webbrowser.open("H:\krish\Coding\Microsoft VS Code\Programmes\playlist\J.xspf")