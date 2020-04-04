#listen and respond test

import pyttsx3
import speech_recognition as sr
  
# initialisation 
engine = pyttsx3.init() 
  
# testing 
engine.say("Hello There! What is your name?") 
engine.runAndWait() 

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Hello" + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
