from . import speakandlisten
import wikipedia

def wiki():
    #taking the input for what to know about
    wikiknowabout = speakandlisten.takeCommand()
    #getting the search results
    wiki_result = wikipedia.summary(wikiknowabout, sentences = 3 or 4)
    print(wiki_result)
    speakandlisten.speak(wiki_result)