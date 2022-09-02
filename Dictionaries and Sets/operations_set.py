# operations on a set
a = {1, 3, 4, 5, 1}
print(type(a))
print(a)

print(len(a))       # prints the length of set

a.remove(1)     # removes the desired element from set
print(a)        # print a after removal of 1

print(a.pop())  # removes an arbitrary(random) element from set
print(a)

print(a.clear())  # clear the set and returns none
