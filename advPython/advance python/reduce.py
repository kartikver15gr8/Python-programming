from functools import reduce
sum = lambda a,b: a+b

l = [1,5,7,9,6,4,545,656]
val = reduce(sum,l)
print(val)
