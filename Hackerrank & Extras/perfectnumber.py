def perfect_number(N):
    sum = 0
    for x in range (1,N):
        if N % x == 0:
            sum += x
    return sum == N
print(perfect_number(6))
