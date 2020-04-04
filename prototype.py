#prototype
import pyttsx3 
import speech_recognition as sr
import modules
import time

# initialisation of test to speach engine
engine = pyttsx3.init() 
engine.setProperty('rate', 165)#normal human speach is about 150 wpm

zipcode = "83440"
user = "John"

def listen_to_user():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #engine.say("Say something")
        #print("Say something!")
        #engine.runAndWait()
        while(cv2.waitKey(25) & 0xFF == ord('q')):#test to see if can do on button press
            audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    return r.recognize_sphinx(audio)


"""
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

def startup():
    startupText = "Hello " + user + ", how are you today?"
    engine.say(startupText)
    engine.runAndWait()
    time.sleep(0)#wait until finished speaking

def main():
    startup()
    userSay = listen_to_user()
    print(userSay)


if __name__ == "__main__":
    # execute only if run as a script
    main()