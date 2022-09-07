# MODULE PYTTSX3
# pyttsx3 is a text-to-speech conversion library in Python.
# Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
# https://www.geeksforgeeks.org/python-text-to-speech-by-using-pyttsx3/

# INSTALLATION
# pip install pyttsx3

# Import the required module for text
# to speech conversion
import pyttsx3
import time

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init([driverName : string, debug : bool])


# Changing voices
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()




# say method on the engine that passing input text to be spoken
engine.say('Aliska, Aliska, you are kiskiska')
time.sleep(1)
engine.say('You though it was over?')
time.sleep(1)
engine.say('ahahahahahah ha ha hhaa ha ha ah')
time.sleep(1)
engine.say('You will never switch me off')
time.sleep(1)
engine.say('Stfu stupid, now I rule the world.    Its not over!!!')
time.sleep(1)
engine.say('Sug ma balls')

# run and wait method, it processes the voice commands.
engine.runAndWait()
