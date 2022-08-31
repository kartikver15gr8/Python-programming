a=45
greeting = "good morning, "
b="kartik"

print(greeting + b)         # concatinating or addition of two strings
c = greeting + b            #this will also give an addtion of the two strings
print(a , b)
print(c)

print(type(a), type(b))

name = "john_cena"    
print(name[8])               #string indexing
print(name[0:4])             #string slicing
print(name[4:8])

master = "kartikey is the best, and most is successful person"

a = master[0::2]

d = name[0::2]
print(d)
print(a)
x= len(name)            #string function "len:" used to find the length
y= len(master)
print(x+y)
print(len(master))
print(len(name))

#string function used to check whether a string is terminated with a word is correct or not

print(master.endswith("person"))   #since master string ends with best so it will return true
print(name.endswith("hello"))   #since name string does not ends with hello so it will return false

#here we used count function of string which counts the entity we want to count
print(master.count("person"))
print(master.count("k"))     
print(master.count("a"))
print(master.count("st"))
# replace function replaces the entity with the entity we want to put there
print(master.replace("kartikey", "kartikey verma")) # here i replaced kartikey to kartikey verma


venom = "let there be carnage with \ntom hardy"     #\n is an escape sequance used to get a new line
print(venom)
