#!/usr/bin/python

#Data header(import module), shebang above.
from time import sleep
from sys import exit
from itertools import permutations
from collections import OrderedDict
import urllib2

#Script header (ASCII art)
print "Advise: run the script on full screen terminal"

print "   "
print "   "

print "  ____  _ _     _              _               _                "
sleep(0.1)         
print " |  _ \(_) |   | |            | |             | |               "
sleep(0.1) 
print " | |_) |_| |_  | |_   _    ___| |__   ___  ___| | _____ _ __    "
sleep(0.1) 
print " |  _ <| | __| | | | | |  / __| '_ \ / _ \/ __| |/ / _ \ '__|   "
sleep(0.1) 
print " | |_) | | |_ _| | |_| | | (__| | | |  __/ (__|   <  __/ |      "
sleep(0.1) 
print " |____/|_|\__(_)_|\__, |  \___|_| |_|\___|\___|_|\_\___|_|      "
sleep(0.1) 
print "                   __/ |                                        "
sleep(0.1) 
print "                  |___/                                         "
sleep(0.1) 
print "ver. ALPHATEST"
print "     "
sleep(3) 

print "  _           _                   _   _                   "
sleep(0.1) 
print " (_)         | |                 | | (_)                  "
sleep(0.1) 
print "  _ _ __  ___| |_ _ __ _   _  ___| |_ _  ___  _ __  ___   "
sleep(0.1) 
print " | | '_ \/ __| __| '__| | | |/ __| __| |/ _ \| '_ \/ __|  "
sleep(0.1) 
print " | | | | \__ \ |_| |  | |_| | (__| |_| | (_) | | | \__ \  "
sleep(0.1) 
print " |_|_| |_|___/\__|_|   \__,_|\___|\__|_|\___/|_| |_|___/  "
sleep(0.1) 
print "                                                                           "

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
print "   "
print "   "
print "   "
print "   "
print "   "
print "   "
print "   "
print "   "

answer = raw_input("Please input the string you want to check, taking into account the instructions: ")
bitly1 = list(answer)
listlen = len(bitly1)   
sleep(1)
if len(bitly1)>6 or len(bitly1)<4:
    exit("Error. String is larger than 6 characters or shorter than 4. Terminating script")
elif " " in bitly1:
    exit("Error. Space detected: Terminating script")        
elif "." in bitly1 or "/" in bitly1 or "-" in bitly1 or "_" in bitly1 or ";" in bitly1 or ":" in bitly1 or "," in bitly1 or "!" in bitly1:
    exit("Error. Rogue input detected. Terminating script.")
else:
    print "   "
    print "   " 
    print "   "
    print "the url string will contain the following characters, in any given order without repeating any colocation twice:"
    print bitly1      
    sleep(3)
    print "   "
    print "   "
    print "   "
    print "   "
    print "All the prossible combinations for the redirect adress calcualted. Generating possible bit.ly adresses."
    sleep(3)
    permutations(answer, listlen)
    iterlist = list(permutations(answer, listlen))
    iterlist = [''.join(map(str,i)) for i in iterlist]
    iterlist = list(OrderedDict.fromkeys(iterlist))
    urllist = [str("http://bit.ly/") +s for s in iterlist]
    urllen = len(urllist)
    for p in urllist: 
        print p
    print "number of possible URLs: " + str(urllen)
    sleep(2)
    print "   "
    print "   "
    print "   "
    print "   "
    print "   "
    print "   "
    
    print "Starting http check. This may take a while"
    for p in urllist:
        req = urllib2.Request(p)
        try:
            resp = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            if e.code == 404:
                print str(p)+ " returns 404 error (Not found). This URL will be removed from the list"
                urllist.remove(p)
            elif e.code == 400 or e.code == 401 or e.code == 403:
                print str(p) + " returns a 400 error (Bad request) or 401/403 error (Unauthorized/forbidden) This URL will be removed fromt the list"
                urllist.remove(p)
            elif e.code == 408:
                print str (p) + " returned a 408 error (request timeout) This URL may or may not be available soon, this URL will be kept in the list"
            elif e.code == 429:
                print str(p) + " returned a 429 error (too many requests). The script may have reached a request limit, abort and try again later"           
            elif 500 <= e.code <= 511:
                print str(p) + " returned a 5xx error (server error). bit.ly servers may be unavailable at the moment. If the error persists abort and try again later"
            elif 410 <= e.code <= 451 or ecode > 511:
                print str(p) + " has returned an unespecified http error. This URL will be removed from the list"
                urllist.remove(p)   
        except urllib2.URLError as e:
             print str(p) + " returned an unespecified error regarding the URL. This URL will be removed from the list"
             urllist.remove(p)
        else:
            # 200
            body = resp.read()
            print str(p) + " returns a 200 status code (Ok). This URL exists."   
urllen = len(urllist)
sleep (3)
print "http status check finished. Printing the approved URLs to the screen now..."
sleep(2)
print"   "
for p in urllist:
    print p
print "   "
print "Number of working URLS: " + str(urllen)
    
