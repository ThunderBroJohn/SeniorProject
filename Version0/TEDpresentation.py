#TEDpresentation.py
import datetime
import time
import pyttsx3

# initialisation of test to speach engine
engine = pyttsx3.init() 
engine.setProperty('rate', 165)#normal human speach is about 150 wpm

def spell_word(word):#QT
    splitWord = ""
    for i in word:
        splitWord += i + " "
    splitWord = splitWord[:-1]
    return splitWord

def check_calander():#QC PASS
    dt = datetime.datetime.today()
    m = dt.month
    month = ""
    d = dt.day
    y = dt.year

    if(m == 1):
        month = "January"
    if(m == 2):
        month = "Febuary"
    if(m == 3):
        month = "March"
    if(m == 4):
        month = "April"
    if(m == 5):
        month = "May"
    if(m == 6):
        month = "June"
    if(m == 7):
        month = "July"
    if(m == 8):
        month = "August"
    if(m == 9):
        month = "September"
    if(m == 10):
        month = "October"
    if(m == 11):
        month = "November"
    if(m == 12):
        month = "December"
    
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

    output = "Today is " + month + " the " + dout +" of " + str(y)
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

def math_module(textInput):#QT
    left, right, mathType = 0, 0, ""
    splitInput = textInput.split()

    saveNumb1 = False

    index = 0
    for word in splitInput:
        if(word.isdigit()):
            if(not saveNumb1):
                left = int(word)
                saveNumb1 = True
            else:
                right = int(word)

        if(word == "plus"):
            mathType = "add"
        if(word == "subtract" or word == "minus"):
            mathType = "subtract"
        if(word == "multiply" or word == "times"):
            mathType = "multiply"
        if(word == "divide" or word == "divided"):
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
    elif(mathType == "intDivison"):
        if(right == 0):
            engine.say("Can not divide by 0")
            engine.runAndWait()
            return None
        solution = int(left) // int(right)
        solution = int(solution)
    elif(mathType == "divide"):
        if(right == 0):
            engine.say("Can not divide by 0")
            engine.runAndWait()
            return None
        solution = left / right
    elif(mathType == "modDivide"):
        if(right == 0):
            engine.say("Can not divide by 0")
            engine.runAndWait()
            return None
        solution = left % right
    out = "The answer is " + str(solution)
    engine.say(out)
    engine.runAndWait()


testInput = "Hey Jake what is the time"

if("the time" in testInput):
    check_time()

testInput = "Hey Jake what is today's date"

if("the time" in testInput):
    check_time()
if("today's date" in testInput):
    check_calander()

testInput = "How do you spell python"

if("spell" in testInput):
    splitInput = testInput.split()

    index = 0
    spellThis = ""
    for word in splitInput:
        if(word == "spell"):
            spellThis = splitInput[index+1]
            break
        index += 1

    spelled = spell_word(spellThis)
    engine.say(spelled)
    engine.runAndWait()

math_module("What is 4 plus 8") #12
math_module("What is 5 subtract 4")
math_module("What is 5 minus 4")
math_module("What is 5 divided by 0")
math_module("what is 23 divide by 10") 
math_module("what is 4 times 5")