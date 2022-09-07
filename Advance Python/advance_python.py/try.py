# # Without try method

# while(True):        # so here we made a while loop which will run until the condition is true for each correct input as mentioned below
#     print("press q to quit")
#     a = input("enter the value of a :")
#     if a=='q':      # Here if the value of "a" which is entered by trhe user is "q" then the lopp will break
#         break
#     a = int(a)      # Here we typecasted the a in as an integer
#     if a>6:
#         print("The value of a is greater than 6")
# print("Thanks for playing!!!!!")

#******************* OR *************

# by using the "try" method

# We have done a same implementation by using true so that 
# if somehow the user enters a wrong input then 
#the try method will not let the program to break 
#bit will tell us the error and then begins to continue again
# while(True):
#     print("press q to quit")
#     a = input("enter the value of a :  ")
#     if a=='q':
#         break
#     try:
#         a = int(a)
#         if a>6:
#             print("The value of a is greater than 6")
#     except Exception as e:
#         print(f"This returns an error as {e}")
# print("Thanks for playing!!!!!")

        

# try:
#     a = input("enter the value of a :")
#     a = int(a)
#     b = 1/a
#     print(b)

# except ValueError as j:
#     print("please check the value u have entered")
# except ZeroDivisionError as q:
#     print("you have entered 'zero' as denometator which is indiscriminant ")

# print("Thanks for playing !!!!")

def Increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("please enter an appropriate value")
a = Increment(364)
print(a)