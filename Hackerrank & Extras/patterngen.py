n = int(input())
even = 0
odd = 0
while (n > 0):
    rem = n % 10
   
    if rem %2==0:
        even = even + rem
    else:
        odd = odd + rem
    n = int (n / 10)

print (even)
print (odd)


    
    

    

    
    
