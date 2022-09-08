def divisible_by_5(a):      # This is the divisibility test of 5 by defining a function
    if a%5 == 0:
        return True
    else:
        return False
def divisible_by_2(a):      # This is the divisibility test of 2 by defining a function
    if a%2 == 0:
        return True
    else:
        return False

divisible_by_3 = lambda a:a%3==0        # This is the divisibility test of 3 by using lambda
divisible_by_7 = lambda a:a%7==0        # This is the divisibility test of 7 by using lambda


numbers = [1,5,7,8,56,7,98,654,56,55,105,20,100]
print(list(filter(divisible_by_5,numbers)))         # This will filter the list numbers and only return those numbers in the list which are divisible by 5
print(list(filter(divisible_by_2,numbers)))         # This will filter the list numbers and only return those numbers in the list which are divisible by 2
print(list(filter(divisible_by_3,numbers)))         # This will filter the list numbers and only return those numbers in the list which are divisible by 3
print(list(filter(divisible_by_7,numbers)))         # This will filter the list numbers and only return those numbers in the list which are divisible by 7divisible_by_7

    