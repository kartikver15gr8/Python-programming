# Strings

# name = input("Enter the name of the user: \n")
# print(f"Good Afternoon {name}")
# def confirmationLetter(Name,Company,date):
#     print(f"Dear {Name},\nYou are selected! for this role we are glad to have you,\n{Company},{date}")
# a = confirmationLetter("Kartikey Verma","Apple","16th sept 2024")
# string = input("Enter the string:\n")
# print(string.count('  '))
# newStr = string.replace("  "," ")
# print(newStr)
# letter = "Dear Kartik,This Python course is nice. Thanks"
# newStr = letter.replace(",","\n")
# # newStr = letter.replace(".","\n")
# print(newStr)

#list and tuples

# fruit1 = input("Enter the fruit1:\n")
# fruit2 = input("Enter the fruit2:\n")
# fruit3 = input("Enter the fruit3:\n")
# fruit4 = input("Enter the fruit4:\n")
# fruit5 = input("Enter the fruit5:\n")
# fruit6 = input("Enter the fruit6:\n")
# fruit7 = input("Enter the fruit7:\n")

# fruits = [fruit1,fruit2,fruit3,fruit4,fruit5,fruit6,fruit7]

# print(fruits)

# m1 = float(input("Enter m1:\n"))
# m2 = float(input("Enter m2:\n"))
# m3 = float(input("Enter m3:\n"))
# m4 = float(input("Enter m4:\n"))
# m5 = float(input("Enter m5:\n"))
# m6 = float(input("Enter m6:\n"))

# marks = [m1,m2,m3,m4,m5,m6]
# marks.sort()
# print(marks)

# tuple1 = (7,0,8,0,0,9)
# print(f"The number of zeros in tuple1 is/are:\n {tuple1.count(0)}")
# def uniq(L):
#     if(len(L)==1):
#         return(L[-1])
#     for i in range(len(L)-1):
#         if(L[i]==L[-1]):
#             L.remove(L[i])
#         return[L[-1] + uniq(L[-1])]
# a = uniq([1,2,3,2,1,4])
# print(a)

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))





