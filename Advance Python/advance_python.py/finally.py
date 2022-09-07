try:
    a = int(input("enter the value of a: "))
    c = 1/a
    print(c)
except Exception as e:
    print(f"Invalid input {e}")
    exit()
finally:   # So basically finally is used to add a termination line(string) to our code
    print("We are done !!")     # This string will run even if the program have an error

