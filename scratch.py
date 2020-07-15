"""
import subprocess


open_sub(inputText):
    path = 'C/'
    cleanPath = path.replace('\\f', '\\\\f')
    subprocess.call([''])

"""
#import random
import pyttsx3
import time

engine = pyttsx3.init() 
engine.setProperty('rate', 165)

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

def talk_to_jake():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

talk_to_jake()
rt = input("letter")
print(rt)
talk_to_jake()