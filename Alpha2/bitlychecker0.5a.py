#!/usr/bin/python

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
print "ver. ALPHATEST"
print "     "
time.sleep(3) 

print "                               _           _                   _   _                   "
time.sleep(0.1) 
print "                              (_)         | |                 | | (_)                  "
time.sleep(0.1) 
print "  _   _ ___  __ _  __ _  ___   _ _ __  ___| |_ _ __ _   _  ___| |_ _  ___  _ __  ___   "
time.sleep(0.1) 
print " | | | / __|/ _` |/ _` |/ _ \ | | '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __|  "
time.sleep(0.1) 
print " | |_| \__ \ (_| | (_| |  __/ | | | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \  "
time.sleep(0.1) 
print "  \__,_|___/\__,_|\__, |\___| |_|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/  "
time.sleep(0.1) 
print "                   __/ |                                                               "
time.sleep(0.1) 
print "                  |___/                                                                "

print "Welcome to bit.ly checker!"
print "This script will take a bunch of letters you input and check each combination of characters to see if they can form part of a bit.ly link! This script will also check if there is a bit.ly link up with that string!"
 

raw_input("Press enter to continue")

print "Please take into account the following input rules:"
print "    "

print "1) Remember that bit.ly links are case sensitive. This  version of the script won't look for both uppercase and lowercase letters link unless they are both on the input list!"

print "    "

raw_input("Press enter to continue")

print "2)Input uppercase and lowercase letters and numbers. Avoid using spaces, hyphens, dots, commas and any other symbol or foreign letter, as bit.ly link only contains letters and numbers. Script will close if detects spaces or special symbols."
print "    "
raw_input("Press enter to continue")

print "3) The minimun number of characters for a string is 4 characters and the maximum is 6. If you have a string with more characters and suspect its a bit.ly link, try deleting one of each of the following letters in your string: b, i, t, l, y. This is for removing the bit.ly part of the url and leave only the redirect adress, which is what this script uses to generate the URLs. "
print "If your url is longer than expected and: you can't remove ONE LETTER OF EACH OF THE ONES stated above,after deleting them your URL is still longer than required, or your string is shorter than required, your string isn't a bit.ly url. The script will return an error code if used with a bad string.
print "    "
raw_input("Press enter to continue")
print "4)The script will add any special punctuation needed"

raw_input("Press enter to run the script")

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
    
    
    
                        
                    

