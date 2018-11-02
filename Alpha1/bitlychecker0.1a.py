#!/usr/bin/python

#Data header below (module import) | Data shebang above.
import time

#Script header (ASCII art)
print "  ____  _ _     _              _               _                "
time.sleep(0.1)         
print " |  _ \(_) |   | |            | |             | |               "
time.sleep(0.1) 
print " | |_) |_| |_  | |_   _    ___| |__   ___  ___| | _____ _ __    "
time.sleep(0.1) 
print " |  _ <| | __| | | | | |  / __| '_ \ / _ \/ __| |/ / _ \ '__|   "
time.sleep(0.1) 
print " | |_) | | |_ _| | |_| | | (__| | | |  __/ (__|   <  __/ |      "
time.sleep(0.1) 
print " |____/|_|\__(_)_|\__, |  \___|_| |_|\___|\___|_|\_\___|_|      "
time.sleep(0.1) 
print "                   __/ |                                        "
time.sleep(0.1) 
print "                  |___/                                         "
time.sleep(0.1) 
print "ver 0.1a"
print "     "
time.sleep(2) 

#Script intro (About)
print "Welcome to bit.ly checker! This script will take a bunch of letters you input and check each combination of characters to see if they can form a bit.ly link!"
print "     "

#Bit.ly alpha script: Asks for input, assign input to answer variable. Assign answer var type to answertype: If answertype (raw_input var type) is a string or an integer, print "Input ok", if its any other var type, print "syntax error, input ok". note: raw input always returns a string
answer = raw_input("Please input the string you want to check, with no spaces bewteen letters ")
answertype = type(answer)
if answertype == str or answertype == int:
    print "input ok"  
else:
    print "syntax error, input ok" 
