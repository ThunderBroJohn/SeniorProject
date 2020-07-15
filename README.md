# Digital Assistant Jake
 A digital assistant meant to assist a user in productivity

Current working main file: Prototype2.py
   supporting files: modules.py, timerAndAlarm.py, mathMod.py

Used libraries
   pyttsx3 - Text to speach
   speachRecognition - speach to text - sphynx
   time, datetime - time management
   threadding - certain processes need to run concurrently
   cv2 - OpenCV
   webbrowser, json, requests, socket - for internet
   psutil - computer utility tool
   math - math
   word2number - tool to convert a scentence of a number into a digit form

Known bugs:
- Math module int division and mod division are having trouble. This is due to python 3.
- bad commands default to "what time is it" instead of "I'm sorry, I don't understand that command"

Planned: If I continue this after college I will make sure to rewrite the whole thing in C++
