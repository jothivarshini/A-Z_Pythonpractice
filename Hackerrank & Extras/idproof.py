import re
aadhar=(input("Enter the number: "))
if re.match("^[0-9]{12}$",aadhar):
    print ("It is a valid aadhar")
else:
    print ("Aadhar is invalid")
    
