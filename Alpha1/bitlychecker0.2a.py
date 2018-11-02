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
print "ver 0.2a"
print "     "
time.sleep(2) 

#Script intro (About)
print "Welcome to bit.ly checker! This script will take a bunch of letters you input and check each combination of characters to see if they can form a bit.ly link!"
print "     "

#Bit.ly alpha script.2: Asks for input, assign input to answer variable. Use list() to separate the string. In each of its conforming letters. Print list check
answer = raw_input("Please input the string you want to check, with no spaces bewteen letters ")
bitly1 = list(answer)
print "printing list. . ."
time.sleep(1)
print bitly1   

