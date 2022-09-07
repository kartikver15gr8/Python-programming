a = [1,2,3,4,5,6,9,8,7,10]       #Here we created a list "a"
b = []                      # Here we created another list "B" which is empty
for item in a:
    if item%2 == 0:
        b.append(item)       # Here we used "append" to add those elements in "B" who are divisible by 2
print(b)

# Here we can also do the same above task by using list comprehension method as done below
b = [items for items in a if items%2==0]
print(b)
