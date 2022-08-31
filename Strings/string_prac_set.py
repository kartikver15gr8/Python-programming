# name = input("enter your name\n")
# print("good morning," +name)

letter = '''dear <|name|>
            you are selected!!
            <|date|>'''


name = input("enter the name\n")
date = input("enter the date\n")

letter = letter.replace("<|name|>" , name)
letter = letter.replace("<|date|>" , date)

print(letter)