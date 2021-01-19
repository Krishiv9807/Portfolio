import webbrowser
from . import speakandlisten

def google_search():
    #defining the chrome path
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    speakandlisten.speak("What search do you want to make Sir?")
    #getting the input for what to search
    query  = speakandlisten.takeCommand()
    #getting the results
    webbrowser.get(chrome_path).open('https://www.google.com/search?q=' + query + '&oq=' + query + '&aqs=chrome..69i57j0j46l2j0j69i61j69i60j69i61.1786j0j9&sourceid=chrome&ie=UTF-8')
    print('https://www.google.com/search?q='+query)
    #webbrowser.get(chrome_path).open('https://www.google.com/search?q='+query)

def youtube_search():
    #defining the url of destination page
    url = 'https://www.google.com/'
    speakandlisten.speak("What search do you want to make Sir?")
    #getting the input for what to searcg
    query = speakandlisten.takeCommand()
    #giving the browser path
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    #getting the web results
    webbrowser.get(chrome_path).open('https://www.youtube.com/results?search_query=' + query)