# Bit.ly-checker
This python script asks the user to input an alphanuemric string (uppercase, lowercase and numbers) of between 4 and 6 letters (the length limit of a bit.ly link) and:
1)Permutate the string to get all possible combinations, makes a list.
2)Appends http://bit.ly/ to each combination of the list.
3)Starts an http code check to see if there is a link up with that combination and:
  a)If it returns a 200 'ok' code, a 429 'too many requests error' or any 5xx 'internal server error' it'll stay in the list
  b)If it returns a:400, 401, 403, 404, 408, 429 or any other http error code not included above, the link will be elinminated          from the list.
4) It returns a list with all links that return a code specified in 3.a)
5)It'll then ask you to choose between:
  a)Close the script and export the list to a txt file (not available yet)
  b)keep running the script to unshorten the links and see where they redirect too. Retuns a list witht he unshortened URLs that can either be exported as a txt file (not available yet) or discarded to close the script.


DISCLAIMER: This script is not completed yet and may be unestable. The http check is not 100% accurate and sometimes can clog the script: If you see the script becomes unresponsive during a http check, use the keyboard interrupt key to close the script.
  
