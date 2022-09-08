def square(a):
    return a*a    
l1=[1,5,7,8,9]

#Method 1: by making another list
# l2 = []
# for item in l1:
#     l2.append(square(item))
# print(l2)

# Method 2: by using map
# print(list(map(square,l1)))