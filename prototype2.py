#prototype2 John Miller Senior Project part B
"""
This is prototype 2, which is a functional digital assistant
utilizing several home made modules that will perform basic functions
that are common to the average user. It accepts text or speach as means
of recognized input.

"""

#prototype 2 imports
import pyttsx3 #important! Use version 2.71
import modules
import time
import timerAndAlarm
import mathMod
import speech_recognition as sr

# initialisation of speach to text engine
r = sr.Recognizer()

# initialisation of text to speach engine
engine = pyttsx3.init() 
engine.setProperty('rate', 165)#normal human speach is about 150 wpm


#default settings
settings = ["John","83440"]

#speak to user
def speak(inputString):
    engine.say(inputString)
    engine.runAndWait()

#speak to jake
def talk_to_jake():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        text = ""
    # recognize speech using Sphinx
    try:
        text = r.recognize_sphinx(audio)
        print("Jake thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        text = "Jake could not understand audio"
    except sr.RequestError as e:
        text = "Jake encountered an error; {0}".format(e)
    return text


#run start up hello
def startup():
    hello =  "Hello " + settings[0] + " welcome to Jake, your digital assistant."
    hello += " Please be sure to speak loudly and clearly so I can understand you."
    speak(hello)


#define main
def main():
    #setup
    startup()
    timer = timerAndAlarm.Timer(0,False)
    alarm = timerAndAlarm.Alarm(False,0,0)
    reminderAlarm = timerAndAlarm.Reminder(False,0,0)
    time.sleep(1)
    speak("When you need me, please press R to speak to me, or press T to type a request as a sentance")
    
    #begin program
    while(True):
        request = ""
        rtype = ""

        #wait for what type of input
        while(rtype != "r" and rtype != "t" and rtype != "q"):
            rtype = ""
            rtype = input("Press r to talk to me, press t to type a request: ")

            if(rtype == "r"):
                request = talk_to_jake()
            elif(rtype == "t"):
                request = input("Please type your request: ")
            elif(rtype == "q"):
                speak("Thank you, have a great day")
                break
        if(rtype == "q"):
            break

        #parser/keyword searching
        if(request == "quit"):
            speak("Thank you, have a great day")
            break
        elif("what can you do" in request):
            menu = "I can perform basic math, check the time and date, google search, "
            menu += "check the weather, open google maps of your current town, "
            menu += "take down a quick note, and run timers and alarms"
            speak(menu)
        elif("add" in request or "plus" in request or "added" in request):
            mathMod.math_module(request)
        elif("subtract" in request or "subtracted" in request or "minus" in request):
            mathMod.math_module(request)
        elif("multiply" in request or "multiplied" in request or "times" in request):
            mathMod.math_module(request)
        elif("divide" in request or "divided" in request):
            mathMod.math_module(request)
        elif("google search" in request):
            modules.google_search(request)
        elif("mirror" in request):
            modules.mirror()
        elif("joke" in request):
            modules.random_joke()
        elif("system" in request):
            status = modules.system_status()
            speak(status)
            print(status)
        elif("spell" in request):
            modules.spelling(request)
        elif("weather" in request):
            modules.check_weather(settings[1])
        elif("open a map" in request or "open map" in request):
            modules.open_map()
        elif("today's date" in request or "day is it" in request or "todays date" in request):
            modules.check_calander()
        elif("set a timer" in request):
            timer.startTimer(modules.timer_prep(request))
        elif("cancel timer" in request):
            timer.cancelTimer()
        elif("set an alarm" in request):
            hour, minute = modules.alarm_prep(request)
            alarm.startAlarm(hour, minute)
        elif("cancel alarm" in request):
            alarm.cancelAlarm()
        elif("create reminder" in request or "create a reminder" in request):
            note, hour, minute = modules.reminder_prep(request)
            reminderAlarm.create_reminder_note(note)
            reminderAlarm.startReminderAlarm(hour, minute)
        elif("create note" in request or "create a note" in request):
            modules.create_note(request)
        elif("what time is it" in request or "what is the time"):
            modules.check_time()
        else:
            speak("I'm sorry I don't know how to do that request")
 
    del timer
    del alarm
    del reminderAlarm


#run program
if __name__ == "__main__":
    # execute only if run as a script
    main()