#!/usr/bin/python

#Data header(import module), shebang above.
import time
import sys
import itertools

#Script header (ASCII art)
print "Advise: run the script on full screen terminal"

print "   "
print "   "

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
 

raw_input("Press enter to open usage instructions")

print "Please take into account the instructions:"
print "    "

print "1) Remember that bit.ly links are case sensitive. This  version of the script won't look for both uppercase and lowercase letters link unless they are both on the input list!"

print "    "


print "2)Input uppercase and lowercase letters and numbers. Avoid using spaces, hyphens, dots, commas and any other symbol or foreign letter, as bit.ly link only contains letters and numbers. Script will close if detects spaces or special symbols. You can use ? as a wildcard for one or more unknown characters"
print "    "

print "3) The minimun number of characters for a string is 4 characters and the maximum is 6. If you have a string with more characters and suspect its a bit.ly link, try deleting one of each of the following letters in your string: b, i, t, l, y. This is for removing the bit.ly part of the url and leave only the redirect adress, which is what this script uses to generate the URLs. "
print "If your url is longer than expected and:"
print "a) you can't remove ONE LETTER OF EACH OF THE ONES stated above"
print "b) after deleting them your URL is still longer than required" 
print "c) your string is shorter than required!"
print "then your string isn't a bit.ly url. The script will return an error code if used with a bad string."
print "    "

print "4)The script will add any special punctuation needed"

raw_input("Press enter to run the script. If you run the script you understand and acknowledge this instructions")

#Bit.ly alpha script.4: Asks for input, assign input to answer variable. Use list(answer) to separate the string In each of its conforming letters. If length does not much print "len error". Elif input contains spaces, print "Error. Spaces detected" and abort. EliF rogue characters, print rogue error.
answer = raw_input("Please input the string you want to check, taking into account the instructions: ")
bitly1 = list(answer)
listlen = len(bitly1)   
time.sleep(1)
if len(bitly1)>6 or len(bitly1)<4:
    sys.exit("Error. String is larger than 6 characters or shorter than 4. Terminating script")
elif " " in bitly1:
    sys.exit("Error. Space detected: Terminating script")        
elif "." in bitly1 or "/" in bitly1 or "-" in bitly1 or "_" in bitly1 or ";" in bitly1 or ":" in bitly1 or "," in bitly1 or "!" in bitly1:
    sys.exit("Error. Rogue input detected. Terminating script.")
else:
    print "the url string will contain the following characters, in any given order without repeating any colocation twice:"
    print bitly1      
    time.sleep(5)
    print "All the prossible combinations for the redirect adress calcualted. Generating bit.ly adresses."
    time.sleep(3)
    itertools.permutations(answer, listlen)
    iterlist = list(itertools.permutations(answer, listlen))
    interlist = [''.join(map(str,i)) for i in iterlist]
    interlist = [str("bit.ly/") +s for s in interlist]
    print interlist
    print "the code follows here"
    
