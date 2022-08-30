# kirana store calculator

sum = 0
while(True):
    l1 = ["hey"]
    user_input = input("Enter the price of purchased product:\n")
    if user_input != 'q':
        l1 = l1.append(user_input)

        sum = sum + int(user_input)
        print(f"The total of purchased items now is {sum}\n")
    else:
        print(f"The total bill is {sum}\n Thanks for shopping with us !!\n Have a nice day")
        print(l1.append)
