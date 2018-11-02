#!/usr/bin/python

#Data header below (module import) | Data shebang above.
import time
import sys

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
print "ver 0.4a"
print "     "
time.sleep(2) 

#Script intro (About)
print "Welcome to bit.ly checker! This script will take a bunch of letters you input and check each combination of characters to see if they can form a bit.ly link!" 
print "Remember that bit.ly links are case sensitive. This  version of the script won't look for both uppercase and lowercase letters link unless they are both on the input list!"
print "     "

#Bit.ly alpha script.4: Asks for input, assign input to answer variable. Use list(answer) to separate the string In each of its conforming letters. If input contains spaces, print "Error. Spaces detected" and abort. Elif input DO NOT contains b, i, t, l and y (upper and/or lowercase), print "Letters B, i, t, l and/or y not detected: impossible to make a bit.ly link." and abort. Else print list #check. Dot prints/waits are for conditional integrity. Do not touch
answer = raw_input("Please input the string you want to check, with no spaces bewteen letters: ")
bitly1 = list(answer)
time.sleep(1)
if " " in bitly1:
    sys.exit("Error. Spaces detected: Terminating script")
else:
    print ". . ."
    time.sleep(0.5)
if "B" in bitly1 or "b" in bitly1:
    print " .. ."
    time.sleep(0.5) 
if "I" in bitly1 or "i" in bitly1:
    print " . .."
    time.sleep(0.5)
if "T" in bitly1 or "t" in bitly1:
    print " . . ."
    time.sleep(0.5) 
if "L" in bitly1 or "l" in bitly1:
    print " . .."
    time.sleep(0.5)
if "Y" in bitly1 or "y" in bitly1:
    print " .. ."
    time.sleep(0.5) 
    print ". . ."
    time.sleep(0.5)
    print"All OK. Printing list. . ."
    time.sleep(1)
    print bitly1
else:   
    sys.exit("Letters B, i, t, l and/or y not detected: impossible to make a bit.ly link. Terminating script")
    

