b={1:[76.1,10.2], 2:[85.6,12.3]}
g={1:[75,9.5], 2:[84.5,11.8]}
age = int(input())
gender=input()
if gender=='b':
    h=b[age] [0]/100
    w=b[age][1]
    bmi=w/h*h
    print(bmi)
elif  gender=='g':
    h=g[age] [0]/100
    w=g[age][1]
    bmi=w/h*h
    print(bmi)
else:
    print ("invalid input")
    
