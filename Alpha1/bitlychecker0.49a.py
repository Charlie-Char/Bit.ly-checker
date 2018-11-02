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

#Bit.ly alpha script.4: Asks for input, assign input to answer variable. Use list(answer) to separate the string In each of its conforming letters. If input contains spaces, print "Error. Spaces detected" and abort. Elif input DO NOT contains b, i, t, l and y (upper and/or lowercase), print "Letters B, i, t, l and/or y not detected: impossible to make a bit.ly link." and abort. Else print list #check. Dot prints/waits are for conditional integrity. Do not touch
answer = raw_input("Please input the string you want to check, taking into account the input rules:")
bitly1 = list(answer)
time.sleep(1)
if " " in bitly1:
    sys.exit("Error. Space detected: Terminating script")
elif len(bitly1)>11 or len(bitly1)<9:
    sys.exit("Error. String is larger than 11 characters or shorter than 9")        
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
                    print"loquesea"
                else:   
                    sys.exit("Letter y and/or other bit.ly letters not detected: impossible to make a bit.ly link: Terminating script")
            else:   
                sys.exit("Letter l and/or other bit.ly letters not detected: impossible to make a bit.ly link: Terminating script")
        else:   
            sys.exit("Letter t and/or other bit.ly letters not detected: impossible to make a bit.ly link: Terminating script")
    else:   
        sys.exit("Letter i and/or other bit.ly letters not detected: impossible to make a bit.ly link: Terminating script")
else:   
    sys.exit("Letter B and/or other bit.ly letters not detected: impossible to make a bit.ly link: Terminating script")
    
    
    
                        
                    

