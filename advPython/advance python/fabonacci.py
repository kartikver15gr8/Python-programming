a1 = 0
a2 = 1

b = int(input("Enter the value of b:\n"))

if b<0:
    print("Enter a valid positive integer\n")
elif b==1:
    print(f"The fabonacci series is {b}")
else:
    print(f"The Fabonacci series for {b} is :")
    for i in range(b):
        print(a1)
        ath = a1+a2
        a1 = a2
        a2 = ath
        i +=1