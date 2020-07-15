#jarvis test run

# importing the pyttsx library 
import pyttsx3 
  
# initialisation 
engine = pyttsx3.init() 
engine.setProperty('rate', 165)#default is 200 wpm human average is 150

engine.say('Would you like to play a game')
engine.runAndWait()
engine.stop()

def disp_menu():
    print("Here is what you can do")
    

def main():
    """ Main function """
    inp = ''
    while(inp != 'q'):
        engine.say('what can I do for you today')
        engine.runAndWait()
        inp = input('What can I do for you today?')






if __name__ == "__main__":
    # execute only if run as a script
    main()