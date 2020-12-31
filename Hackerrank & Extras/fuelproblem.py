d=int(input('Enter the distance of the trip:'))
m=int(input('Enter miles per gallon:'))
gas = d / m
print (gas)

gcost = int(input('Enter the cost per gallon:'))
cost = gcost * gas
print (cost)
