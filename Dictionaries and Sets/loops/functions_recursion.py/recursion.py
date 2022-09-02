# program for factorial

# n = int(input("enter the value of n\n"))
# factorial=1
# for i in range(n):          # so basically this the normal way of making a program of factorial by using loops
#     factorial=factorial*(i+1)
# print(factorial)


# now using recursion for making a program of factorial 

def factorial(n):               # here we firstly defined a recursive function "factorial"
    if n==1 or n==0:    # if n has a value of either 1 or 0 then it will return 1
        return 1
    else:
        return n*factorial(n-1)     # if n is having a value different from 0 or 1 then it will return factorial of that number by doing "n*factorial(n-1)"
print(factorial(6)) # here we can input the value of n under the parenthesis placed after factorial



