marvel = {
    "steve" : "captain america",
    "stark" : "ironman",
    "banner": "hulk",                   # here we created firstly a dictionary marvel
    "thor"  : "chris hemsworth",
  "strange" : "doctor strange",
        0   : 1
}

# method 1
# .Keys                         // this method is used to call all the keys of 
#                               //dictionary and show it in the form of list
print(marvel.keys())        # printing the keys
print(type(marvel.keys()))  # typecasting to check the type variable assigned 
print(list(marvel.keys()))  # converting it into a list and also printing it

# method 2
# .values          // this method is used to call the elements stored in the keys of the dictionary   

print(marvel.values())      # printing the values assigned to the keys of the dictionary

# method 3
# .items        // this method is used to get the dictionary keys along with the elements stored in it

print(marvel.items())       # printing the contents of dictionary

# method 4
# .update               // used to add or update key in the current dictionary

print(marvel)
updatedict = {
    "black widow": "scarlett johansson",  # these are the keys and values added to marvel dictionary
    "wanda"      : "scarlett witch",
    "thor"       : "chris"                  # here we updated thor to chris
}

marvel.update(updatedict)  
print(marvel)              # printing the updated dictionary(marvel) 

# method 5
# .get                          // it is also used to print values stored in keys but if the key 
#                               // is not present it will return none instred of an error

print(marvel["steve"])              # here we are printing the value stored in the key steve as usual
print(marvel.get("steve"))      # here we are printing the value stored in the key steve by using get method
                             #  so that if the key is not present it will return none instead of an error just because of get method
print(marvel.get("harry"))   # here since the key harry is not present so just because of get method it will return none  
