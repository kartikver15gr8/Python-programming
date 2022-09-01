##  There are so many list methods out of which the most common and the methods having more utility are given below;

#method 1: list sorting

numbers = [4,6,8,2,1,3,9,7]
print(numbers)
numbers.sort()      #sorting list "numbers" by using "list sort" method
print(numbers)      # now we will get the sorted list

#method 2: list reversing

numbers.reverse()   #reversing the list
print(numbers)
numbers.reverse()       #again reverses the list

#method 3: list appending

numbers.append(94)  #adds 94 at the end of the list
numbers.append(99)  #adds 99 at the end of the list
numbers.append(97)  #adds 97 at the end of the list
print(numbers)

#method 4: list insertion at desired index

numbers.insert(3, 47)    #it will insert 47 at the index 3
print(numbers)

#method 5: list poping(removes the element of our desired index from the list)

numbers.pop(5)      #remove the element which is on the index 5
print(numbers)

#method 6: list removing(removes the desired element from the list)

numbers.remove(47)  #removes 47 from list
print(numbers)


