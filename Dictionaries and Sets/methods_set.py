# method 1
# .add

babbu = {45,89,97}          # created a set
print(babbu)            # printing it

babbu.add(100)      #  here using add method we added 100 into babbu set 
babbu.add(1000)     #  here using add method we added 1000 into babbu set

print(babbu)        # printing updated babbu set

a = set()       # creating an empty set

a.add(44)               # here we added some elements in empty set a
a.add(45)
a.add(46)
a.add(47)
print(a)                # printing set a
#a.add([45,64,49,0])   # we cannot add a list or dictionary into a set
a.add((43,89,0,36,100))  # but we can add tuples into a set 
print(a)