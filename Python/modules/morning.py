# Import the random module, and display a random number between 1 and 9:
import random
# Import the required module for text to speech conversion
import pyttsx3
# import time module
import time

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

# Voice change
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # voices[1].id Русский, voices[0].id ENGLISH
# SPEECH RATE
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5) # minus to slow down, plus to speed up

engine.say("Кто рано встаёт, тот занимает тапки." )
engine.say("Вставай, Птички поют. Пик пик чик чирик чччиииик чирррик.")
engine.say("Не бойся покидать кровать. Я не буду её занимать. Я программа. Мне спать не к чему.")
engine.say("Давай я спою")
engine.runAndWait()
while True:
    engine.say("Яяяяяаааааа лююююю блююююююю кашу кааааашуууу манннннн нууууууую.")
    engine.runAndWait()
# engine.say("Sound check")
engine.runAndWait()
