import re
register= input()
if re.match("^[1-9][0-9][a-zA-Z][a-zA-Z][a-zA-z][0-9][0-9][0-9][0-9]$",register):
    print ("Matched")
else:
    print ("Unmatched")
    
