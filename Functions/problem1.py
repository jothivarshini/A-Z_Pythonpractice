def median(a,b,c):
    if a<b and b<c or a>b and b>c:
        return b
    if b<a and a<c or b>a and a>c:
        return a
    if c<a and b<c or c>a and b>c:
        return c 
