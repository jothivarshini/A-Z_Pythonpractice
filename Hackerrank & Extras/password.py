import re
password = input()
flag = 0
while True:
    if(len(password)<8):
        flag = -1
        break
    elif re.search ("[a-z]",password):
        flag = -1
        break
    elif re.search ("[A-Z]",password):
        flag = -1
        break
    elif re.search ("[1-9]",password):
        flag = -1
        break
    elif re.search ("[~!@#$%^&*()_+]",password):
        flag = -1
        break
    elif re.search("\s",password):
        flag = -1
        break 
    else:
        flag = 0
        print ("valid password")
        break
if flag ==-1:
    print ("invalid password")
