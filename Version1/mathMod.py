
import math
import pyttsx3
from word2number import w2n

# initialisation of test to speach engine
engine = pyttsx3.init() 
engine.setProperty('rate', 165)#normal human speach is about 150 wpm

def intdiv(a,b):
    return a // b
def moddiv(a,b):
    return a % b 

valid = ['zero','one','two','three','four','five','six','seven','eight',
    'nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',
    'eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty',
    'ninety','hundred','thousand','million','billion','point','and']


def word_to_numeric(textInput):
    splitInput = textInput.split()
    word = ""
    number1 = 0
    numberStr1 = ""
    number2 = 0
    numberStr2 = ""
    vcount = 0

    #print(splitInput)

    for item in splitInput:
        if(item.isdigit()):
            vcount += 1
        if(vcount == 2):
            return textInput
    vcount = 0
    unvalList = []
    count = 0

    #print(splitInput)

    for item in splitInput:
        if item not in valid:
            unvalList.append(count)
        else:
            break
        count += 1
    if(len(unvalList) != 0):
        del splitInput[0:len(unvalList)] #???

    #print(splitInput)

    count = 0
    middle = ""
    for item in splitInput:
        if item not in valid:
            middle += item + " "
        if(vcount == 0): #look for first number
            if item in valid:
                numberStr1 += splitInput[count] + " "
            else:
                vcount = 1
        if(vcount == 1):
            if item in valid:
                numberStr2 += splitInput[count] + " "
        count += 1

    number1 = w2n.word_to_num(numberStr1)
    number2 = w2n.word_to_num(numberStr2)

    result = str(number1) + " " + middle + str(number2)
    return result



def math_module(textInput):#QT
    textInput = word_to_numeric(textInput)

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

"""
test = "what is 5 plus 7"
print(word_to_numeric(test))
math_module(test)

test = "what is seven hundred twenty seven plus two million"
print(word_to_numeric(test))
math_module(test)

#test = "what is two plus two billion and one"
#print(word_to_numeric(test))
#math_module("what is two plus two")
"""