#jarvis scratch

# importing the pyttsx library 
import pyttsx3 
import speech_recognition as sr

# initialisation 
engine = pyttsx3.init() 


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Say something")
    print("Say something!")
    engine.runAndWait()
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

"""
# testing 
engine.say("My first code on text-to-speech") 
engine.say("Thank you, Geeksforgeeks") 
engine.runAndWait() 

def onStart(): 
   print('starting') 
  
def onWord(name, location, length): 
   print('word', name, location, length) 
  
def onEnd(name, completed): 
   print('finishing', name, completed) 
  
#engine = pyttsx3.init() 
  
engine.connect('started-utterance', onStart) 
engine.connect('started-word', onWord) 
engine.connect('finished-utterance', onEnd) 
  
sen = 'Geeks for geeks is a computer portal for Geeks'
  
  
engine.say(sen) 
engine.runAndWait() 

voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()
    """