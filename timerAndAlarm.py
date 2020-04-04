import time
import datetime
import pyttsx3 #important! Use version 2.71
import threading

# initialisation of test to speach engine
engine = pyttsx3.init() 
engine.setProperty('rate', 165)#normal human speach is about 150 wpm


#class threadWrapper(object, threading.Thread):
#    def run(self):
#        object.__init__



class Timer:
    timerRunning = False
    timeRequest = 0
    t1 = None
    
    def __init__(self,timeRequest,timerRunning):
        self.timeRequest = timeRequest
        self.timerRunning = timerRunning
        #print("timer created")

    def cancelTimer(self):
        if(self.timerRunning == False):
            engine.say("The timer is not running")
            engine.runAndWait()
            return
        else:
            self.timerRunning = False
            self.timeRequest = 0
            engine.say("Timer canceled")
            engine.runAndWait()
            self.t1._stop()

    def runTimer(self):
        while(self.timerRunning): #timer is running
            if(self.timeRequest > 0):
                #print(self.timeRequest)
                time.sleep(1)
                self.timeRequest = self.timeRequest - 1
            else:
                self.timerRunning = False
                engine.say("Timer has finished")
                engine.runAndWait()
                break
    
    def run(self):
        self.t1 = threading.Thread(target=self.runTimer)
        self.t1.start()

    def startTimer(self,timeRequestIn):
        self.timerRunning = True
        self.timeRequest = timeRequestIn
        #print("timer started")
        engine.say("Starting the timer")
        engine.runAndWait()
        self.run()

    # def timeLeft(self):
    #    pass

class Alarm:
    alarmRunning = False
    timeGoal = [0,0]
    t1 = None
    
    def __init__(self,alarmRunning,timeGoalHour,timeGoalMinute):
        self.alarmRunning = alarmRunning
        self.timeGoal[0] = timeGoalHour
        self.timeGoal[1] = timeGoalMinute
        #print("alarm created")

    def cancelAlarm(self):
        if(self.alarmRunning == False):
            engine.say("The alarm is not set")
            engine.runAndWait()
        else:
            self.alarmRunning = False
            self.timeGoal = None
            engine.say("Alarm canceled")
            engine.runAndWait()
            self.t1._stop()

    def runAlarm(self):
        while(self.alarmRunning): #alarm is running
            if(self.timeGoal[0] == datetime.datetime.now().hour and self.timeGoal[1] == datetime.datetime.now().minute):
                self.timerRunning = False
                engine.say("Alarm time has been reached")
                engine.runAndWait()
                break
            else:
                pass
                #print("alarm running")

    def run(self):
        t1 = threading.Thread(target=self.runAlarm)
        t1.start()

    #def timeLeft(self):

    def startAlarm(self,requestHour,requestMinute):
        self.alarmRunning = True
        self.timeGoal[0] = requestHour
        self.timeGoal[1] = requestMinute
        engine.say("The alarm is set")
        engine.runAndWait()
        self.run()


class Reminder(Alarm):
    def __init__(self,alarmRunning,timeGoalHour,timeGoalMinute):
        Alarm.__init__(self,alarmRunning,timeGoalHour,timeGoalMinute)

    def create_reminder_note(self,textInput):
        splitInput = textInput.split()

        index = 0
        noteThis = []
        for word in splitInput:
            if(word == "note"):
                noteThis = splitInput[index+1:]
                break
            index += 1
        joinedNote = " "
        joinedNote = joinedNote.join(noteThis)

        #Fix to relative path!
        f = open("C:/Users/jdmdo/Desktop/ComputerVison/SeniorProject/reminders/reminder.txt","w") 
        f.write(joinedNote)
        f.close()

    def read_reminder_note(self):
        #Fix to relative path!
        f = open("C:/Users/jdmdo/Desktop/ComputerVison/SeniorProject/reminders/reminder.txt","r")
        reminder = "reminder! "
        reminder += f.read()
        engine.say(reminder)
        engine.runAndWait()
        f.close()

    def runAlarmReminder(self):
        while(self.alarmRunning): #alarm is running
            if(self.timeGoal[0] == datetime.datetime.now().hour and self.timeGoal[1] == datetime.datetime.now().minute):
                self.timerRunning = False
                engine.say("Reminder time has been reached")
                engine.runAndWait()
                self.read_reminder_note()
                break

    def runReminder(self):
        t1 = threading.Thread(target=self.runAlarmReminder)
        t1.start()

    def startReminderAlarm(self,requestHour,requestMinute):
        self.alarmRunning = True
        self.timeGoal[0] = requestHour
        self.timeGoal[1] = requestMinute
        engine.say("The alarm is set")
        engine.runAndWait()
        self.runReminder()

#testing     
#timerRunning = False
#aTimer = Timer(0,False)
#aTimer.startTimer(30)
#time.sleep(3)
#aTimer.cancelTimer()
#del aTimer


#aAlarm = Alarm(False,0,0)
#aAlarm.startAlarm(16,6)
#time.sleep(3)
#aAlarm.cancelAlarm()
#del aAlarm