"""
These are modules or


"""
from __future__ import division
import pyttsx3 
#import speech_recognition as sr
import time
from threading import Thread
import datetime
import numpy as np
import matplotlib.pyplot as plt
import cv2
import webbrowser
import requests
import json
#import geocoder
import socket
#import timerAndAlarm

# initialisation of test to speach engine
engine = pyttsx3.init() 
engine.setProperty('rate', 165)#normal human speach is about 150 wpm

def intdiv(a,b):
    return a // b
def moddiv(a,b):
    return a % b
def math_module(textInput):#QT
    left, right, mathType = 0.0, 0.0, ""
    splitInput = textInput.split()

    saveNumb1 = False

    index = 0
    for word in splitInput:
        if(word.isdigit()):
            if(not saveNumb1):
                left = float(word)
                saveNumb1 = True
            else:
                right = float(word)

        if(word == "plus" or word == "add" or word == "added"):
            mathType = "add"
        if(word == "subtract" or word == "minus" or word == "subtracted"):
            mathType = "subtract"
        if(word == "multiply" or word == "multiplied" or word == "times"):
            mathType = "multiply"
        if(word == "devide" or word == "divided"):
            if(splitInput[index-1] == "intiger"):
                mathType = "intDivision"
            elif(splitInput[index-1] == "mod" or splitInput[index-1] == "modulus"):
                mathType = "modDivision"
            else:
                mathType = "divide"
    index += 1

    solution = 0
    if(mathType == "add"):
        solution = left + right
    if(mathType == "subtract"): 
        solution = left - right
    elif(mathType == "multiply"):
        solution = left * right
    elif(mathType == "divide"):
        if(right == 0):
            engine.say("Can not divide by 0")
            engine.runAndWait()
            return None
        else:
            solution = left / right
    elif(mathType == "intDivison"):#python is having a lot of trouble with this
        if(right == 0):
            engine.say("Can not divide by 0")
            engine.runAndWait()
            return None
        else: 
            solution = intdiv(left,right)
            #solution = int(solution)
    elif(mathType == "modDivide"):#python is having a lot of trouble with this
        if(right == 0):
            engine.say("Can not divide by 0")
            engine.runAndWait()
            return None
        else:
            solution = moddiv(left,right)

    print(left, right, solution)
    out = "The answer is " + str(solution)
    engine.say(out)
    engine.runAndWait()

def mirror():#QC PASS
    engine.say("press q to quit the mirror")
    engine.runAndWait()
    cap = cv2.VideoCapture(0)  # Pull live video from camera
    while(True):
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow('frame', frame)
        # Wait for 'q' to quit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def check_calander():#QC PASS
    dt = datetime.datetime.today()
    m = dt.month
    month = ""
    d = dt.day
    y = dt.year
    dow = dt.today().weekday()
    weekday = ""

    if(m == 1):
        month = "January"
    elif(m == 2):
        month = "Febuary"
    elif(m == 3):
        month = "March"
    elif(m == 4):
        month = "April"
    elif(m == 5):
        month = "May"
    elif(m == 6):
        month = "June"
    elif(m == 7):
        month = "July"
    elif(m == 8):
        month = "August"
    elif(m == 9):
        month = "September"
    elif(m == 10):
        month = "October"
    elif(m == 11):
        month = "November"
    elif(m == 12):
        month = "December"
    
    if(dow == 0):
        weekday = "Monday"
    elif(dow == 1):
        weekday = "Tuesday"
    elif(dow == 2):
        weekday = "Wednesday"
    elif(dow == 3):
        weekday = "Thursday"
    elif(dow == 4):
        weekday = "Friday"
    elif(dow == 5):
        weekday = "Saturday"
    elif(dow == 6):
        weekday = "Sunday"

    dout = ""

    if(int(d) >= 30):
        dout += "thirty"
    elif(int(d) >= 20):
        dout += "twenty"

    if(int(d) % 10 == 1 and int(d) != 11):
        dout += " first"
    elif(int(d) % 10 == 2 and int(d) != 12):
        dout += " second"
    elif(int(d) % 10 == 3 and int(d) != 13):
        dout += " third"
    elif(int(d) % 10 == 4 and int(d) != 14):
        dout += " fourth"
    elif(int(d) % 10 == 5 and int(d) != 15):
        dout += " fifth"
    elif(int(d) % 10 == 6 and int(d) != 16):
        dout += " sixth"
    elif(int(d) % 10 == 7 and int(d) != 17):
        dout += " seventh"
    elif(int(d) % 10 == 8 and int(d) != 18):
        dout += " eighth"
    elif(int(d) % 10 == 9 and int(d) != 19):
        dout += " nineth"
    elif(int(d) == 10):
        dout += " tenth"
    elif(int(d) == 11):
        dout += " eleventh"
    elif(int(d) == 12):
        dout += " twelfth"
    elif(int(d) == 13):
        dout += " thirteenth"
    elif(int(d) == 14):
        dout += " fourteenth"
    elif(int(d) == 15):
        dout += " fifteenth"
    elif(int(d) == 16):
        dout += " sixteenth"
    elif(int(d) == 17):
        dout += " seventeenth"
    elif(int(d) == 18):
        dout += " eighteenth"
    elif(int(d) == 19):
        dout += " nineteenth"

    output = "Today is " + weekday + " " + month + " the " + dout +" of " + str(y)
    engine.say(output)
    engine.runAndWait()

def check_time():#QC PASS
    dt = datetime.datetime.now()
    h = dt.hour
    m = dt.minute
    ampm = ""
    if(dt.hour >= 12):
        ampm = " P M"
    else:
        ampm = " A M"
    hour = 0
    if(h != 12):
        hour = h % 12
    elif(h == 24 or h == 12):
        hour = 12
    if(m != 0):
        output = "The current time is " + str(hour) + " " + str(m) + ampm
    else:
        output = "The current time is " + str(hour) + ampm
    #output = str(now)
    engine.say(output)
    engine.runAndWait()

def spell_word(word):#QT
    splitWord = ""
    for i in word:
        splitWord += i + " "
    splitWord = splitWord[:-1]
    return splitWord
def spelling(textInput):
    splitInput = textInput.split()

    index = 0
    spellThis = ""
    for word in splitInput:
        if(word == "spell"):
            spellThis = splitInput[index+1]
            break
        index += 1
    speltOut = spell_word(spellThis)
    print(speltOut)
    out = spellThis + " is spelt " + speltOut
    engine.say(out)
    engine.runAndWait()

def lookup(term):#will require internet connection #QT
    #uses import webbrowser 
    #term.replace(" ", "+")
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.open(url, new=0, autoraise=True)
def google_search(textInput):
    splitInput = textInput.split()

    index = 0
    searchThis = []
    for word in splitInput:
        if(word == "search"):
            searchThis = splitInput[index+1:]
            break
        index += 1
    #print(searchThis)
    joinedSearch = "+"
    joinedSearch = joinedSearch.join(searchThis)
    #print(joinedSearch)
    lookup(joinedSearch)

#Weather API by https://rapidapi.com/interzoid/api/us-weather-by-zip-code/details
def check_weather(zipcode):
    url = "https://us-weather-by-zip-code.p.rapidapi.com/getweatherzipcode"

    querystring = {"zip":zipcode}

    headers = {
        'x-rapidapi-host': "us-weather-by-zip-code.p.rapidapi.com",
        'x-rapidapi-key': "0d457b3ee5msh9c4787896992fdap162d3cjsn687ca557f985"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    """
    RESPONCE EXAMPLE JSON response.text
    {"City":"Rexburg","State":"ID","TempF":"45.0","TempC":"7.2","Weather":"A Few Clouds",
    "WindMPH":"16.1","WindDir":"Southwest","RelativeHumidity":"56",
    "VisibilityMiles":"10.00","Code":"Success","Credits":"499871724"}
    """
    #response = '{"City":"Rexburg","State":"ID","TempF":"45.0","TempC":"7.2","Weather":"A Few Clouds","WindMPH":"16.1","WindDir":"Southwest","RelativeHumidity":"56","VisibilityMiles":"10.00","Code":"Success","Credits":"499871724"}'
    #print(response.text)
    output = json.loads(response.text)

    outString = "The weather in " + output["City"] + " is " + output["TempF"]
    outString += " Fahrenheit, conditions look like " + output["Weather"]
    engine.say(outString)
    engine.runAndWait() 

def open_map():
    url = "https://www.google.com/maps/"
    webbrowser.open(url, new=0, autoraise=True)

def timer_prep(textInput):
    splitInput = textInput.split()

    convertedTime = 0
    index = 0
    for word in splitInput:
        if(word == "hour" or word == "hours"):
            if(splitInput[index-1] == "an"):
                convertedTime += (1 * 60 * 60)
            elif(splitInput[index-1] == "half"):##Need to fix so you can say two and a half hours
                if(splitInput[index-3] == "and"):
                    convertedTime += (int(splitInput[index-4]) * 60 * 60)
                convertedTime += (1 * 60 * 30)
            else:
                convertedTime += (int(splitInput[index-1]) * 60 * 60)
        if(word == "minute" or word == "minutes"):
            if(splitInput[index-1] == "a"):
                convertedTime += (1 * 60)
            else:
                convertedTime += (int(splitInput[index-1]) * 60)
        if(word == "second" or word == "seconds"):
            if(splitInput[index-1] == "a"):
                convertedTime += 1
            else:
                convertedTime += int(splitInput[index-1])
        index += 1
    return convertedTime

def alarm_prep(textInput):
    splitInput = textInput.split()
    hour = 0
    minute = 0
    AMPM = False
    index = 0
    for word in splitInput: #look for hour and min time
        if(word.isdigit()):
            number = int(word)
            hour = number // 100
            minute = number % 100
            if(splitInput[index+1] == "P" or splitInput[index+1] == "PM"):
                AMPM = True
        index += 1
    if(AMPM):
        hour = hour + 12
    return hour, minute


#h, m = alarm_prep("set an alarm for 530 PM")
#print(h,m)

def create_note(textInput):
    splitInput = textInput.split()

    index = 0
    noteThis = []
    for word in splitInput:
        if(word == "note"):
            noteThis = splitInput[index+1:]
            break
        index += 1
    #print(searchThis)
    joinedNote = " "
    joinedNote = joinedNote.join(noteThis)

    #Fix to relative path!
    f = open("C:/Users/jdmdo\Desktop/ComputerVison/SeniorProject/notes/notes.txt","a") 
    f.write(joinedNote)
    f.close()
    engine.say("Note created")
    engine.runAndWait()

def reminder_prep(textInput):
    splitInput = textInput.split()
    hour = 0
    minute = 0
    AMPM = False


    index = 0
    noteThis = []
    for word in splitInput:
        if(word == "reminder"):
            noteThis = splitInput[index+1:-2]
        if(word == "at"):
            number = int(splitInput[index+1])
            hour = number // 100
            minute = number % 100
            if(splitInput[index+1] == "P" or splitInput[index+1] == "PM"):
                AMPM = True
        index += 1
    if(AMPM):
        hour = hour + 12

    joinedNote = " "
    joinedNote = joinedNote.join(noteThis)
    return joinedNote, hour, minute
    



