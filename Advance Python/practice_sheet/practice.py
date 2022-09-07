# abhi = "hello how are u , its me buddy"
# print(len(abhi))

# string = "google.com"
# print(string.count("g"))
# print(string.count("o"))
# print(string.count("l"))
# print(string.count("e"))
# print(string.count("."))
# print(string.count("c"))
# print(string.count("m"))

# jojo = "w3resource"
# king = (jojo[:2]+jojo[8:10])
# print(king)

# a = int(input("enter the value of a: \n"))
# b = int(input("enter the value of b: \n"))

# try:
#     print(f"The division of a and b is {a/b}")
# except ZeroDivisionError:
#     print("As the value of b is 0 , therefore the result is infinity ")


from os import write


a = int(input("Enter the value of a: \n"))
Table = [a*i for i in range(0,11)]
print(Table)

with open(Table.txt,"a") as f:
    f.write(str(Table))


