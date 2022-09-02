kartikdictionary={
    "kartik": "data scientist",
    "water": "essential",                   # we can store string
     "mydict" :{'eleven':'number'},         # we can also store another dictionary in one dictionary 
     "marks" : [2,5,8]              # we can also store list in a dictionary
}

print(kartikdictionary['kartik'])
print(kartikdictionary['water'])
print(kartikdictionary['mydict'])
print(kartikdictionary['marks'])


dictionary = {                          # creating another dictionary
    "champu" : "chutiya",
    "mate"   : [45,98,97,100],
    "friends": {'bouncer' : 'yaar'}     # here we created another dictionary(friends) inside a dictionary(dictionary)
}

print(dictionary['mate'])
print(dictionary['champu'])
print(dictionary['friends']['bouncer'])     # printing the element of the friend dictionary 

dictionary['mate']=[98,99,100]              # so here we can see that the keywords are mutable or can be changed
                                            # here we changed the contents of mate list
print(dictionary['mate'])                   # printing the mate list