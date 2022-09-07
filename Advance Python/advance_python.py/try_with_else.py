try:
    a = int(input("enter the value of a: "))
    c = 1/a
    print(c)
except Exception as e:
    print(f"Invalid input {e}")

else:      
    print("The program executed successfully!! ")

 # So basically here the else is used to
 # check whether the program has an error or not , 
 # if the program get executeds and it don't prints the else statement the it means that it was having an error 
 # but if it also prints the else statement after the execution of the program
 # it means that we have successfully made our program and it doesn't have any error 