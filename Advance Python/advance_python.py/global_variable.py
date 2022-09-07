# a = 1080                    # Global variable
# def func1():
#     a = 2160        # Local variable
#     print(a)        # this will print the local variable but 
#                     # that doesn't mean that the global variable 
#                     # is changed because the globle variable will remain unchanged

# func1()     # This will return the local variable ads we have made a local variable in the func1
# print(a)        # This will return the Global variable as the real value of a which is assigned at the topmost is not changed

#********************************************* OR **************************


# To change the Global variable in a program we can do is as below mwntioned

a = 1080                    # Global variable
def func1():
    global a          # Here we used the Global keyword to change "a"
    print(a)
    a = 2160        # Now after using the global keyword above and by assigning diff value to "a" we changed the global variable "a"
    print(a)              
func1()     
print(a)


