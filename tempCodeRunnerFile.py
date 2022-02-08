N = int(input("500,000"))
Sum = 0
for x in range (0, N+1):
    if(x % 2 != 0):
        Sum = Sum + x
print(Sum)