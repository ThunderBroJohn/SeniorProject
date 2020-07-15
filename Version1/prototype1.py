#prototype1 John Miller Senior Project part A
"""
This is prototype 1, which will be a functional digital assistant
utilizing several home made modules that will perform basic functions
that are common to the average user.

Prototype 2 for the first half of next semester will impliment
sphynx voice recognition speach to text for user input. Due to 
the complexity of training the speach recognition with principles
of machine learning, and that it does not work compleatly out of
the box, I have decided to get this prototype working 

"""

#prototype 1 imports
import pyttsx3 #important! Use version 2.71
import modules
import time
import timerAndAlarm

# initialisation of test to speach engine
engine = pyttsx3.init() 
engine.setProperty('rate', 165)#normal human speach is about 150 wpm


#default settings
settings = ["John","83440"]

#speak to user
def speak(inputString):
    engine.say(inputString)
    engine.runAndWait()

#run start up hello
def startup():
    hello = "Hello " + settings[0] + " welcome to Jake, your digital assistant"
    speak(hello)


#define main
def main():
    startup()
    timer = timerAndAlarm.Timer(0,False)
    alarm = timerAndAlarm.Alarm(False,0,0)
    reminderAlarm = timerAndAlarm.Reminder(False,0,0)
    time.sleep(1)
    speak("When you need me, please type a request as a sentance")
    while(True):

        
        request = input()

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
            modules.math_module(request)
        elif("subtract" in request or "subtracted" in request or "minus" in request):
            modules.math_module(request)
        elif("multiply" in request or "multiplied" in request or "times" in request):
            modules.math_module(request)
        elif("divide" in request or "divided" in request):#Currently can not int or mod divide
            modules.math_module(request)
        elif("google search" in request):
            modules.google_search(request)
        elif("mirror" in request):
            modules.mirror()
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