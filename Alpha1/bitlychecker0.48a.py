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
print "ver 0.48a"
print "     "
time.sleep(2) 

#Script intro (About)
print "Welcome to bit.ly checker!"
print "This script will take a bunch of letters you input and check each combination of characters to see if they can form a bit.ly link! This script will also check if there is a bit.ly link up with that string!" 
print "   "
print "   "
time.sleep(5)
print "Please take into account the following input rules:"
print "    "
print "1) Remember that bit.ly links are case sensitive. This  version of the script won't look for both uppercase and lowercase letters link unless they are both on the input list!"
time.sleep(3)
print "2)Input uppercase and lowercase letters and numbers. Avoid using spaces, hyphens, dots, commas and any other symbol or foreign letter, as bit.ly link only contains letters and numbers. Script will close if detects spaces. Otherwise it will try to generate a link, even if it contains special symbols. This will make all generated URLs non-functional. User discretion advised"
time.sleep(3)
print "3) In this version of the script, letters: b, i, t, l and y need to be inside the string provided, otherwise it'll return an error code. The minimun number of characters for the string is 9 characters. (5 characters for 'bit.ly' and another 4 characters, the minimum number of charaters required to make a functional bit.ly link) and the maximum is 11 (5 + 6 maximum characters required to make a functional bit.ly link)"
time.sleep(3) 
print "4)The script will add any special punctuation needed"
time.sleep (5)
print "     "

#Bit.ly alpha script.4: Asks for input, assign input to answer variable. Use list(answer) to separate the string In each of its conforming letters. If input contains spaces, print "Error. Spaces detected" and abort. Elif input DO NOT contains b, i, t, l and y (upper and/or lowercase), print "Letters B, i, t, l and/or y not detected: impossible to make a bit.ly link." and abort. Else print list #check. Dot prints/waits are for conditional integrity. Do not touch
answer = raw_input("Please input the string you want to check, taking into account the input rules:")
bitly1 = list(answer)
time.sleep(1)
if " " in bitly1:
    sys.exit("Error. Space detected: Terminating script")
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
    sys.exit("Letters B, i, t, l and/or y not detected: impossible to make a bit.ly link: Terminating script")
    

