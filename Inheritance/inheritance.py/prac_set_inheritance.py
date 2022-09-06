# class C2dvector():    # Here we created a class for 2d vectors

#     def __init__(self,i,j): # we used the init funtion her tro define i and j
#         self.i =i
#         self.j =j
#     def __str__(self):      # here we used the string funtion to add a "f-String"
#         return f"{self.i}i + {self.j}j is the 2d vector"

# class C3dvector(C2dvector):     # here we made another class for 3d vectors which will inherit from the class C2dvector
#     def __init__(self, i, j, k):
#         super().__init__(i, j)      # Here we used the uper method to access the entities i and j in this class
#         self.k = k          # Here we defined the k 
#     def __str__(self):      # Here we again used the super method to prin the "f-String"
#         return f"{self.i}i + {self.j}j + {self.k}k is the 3d vector"

# c2dvec = C2dvector(2,5)     # here we created an object in the class C2dvector and also provided the desired values to i & j 
# c3dvec = C3dvector(1,5,8)   # here we created an object in the class C3dvector and also provided the desired values to i j and k
# print(c2dvec) # Here we 2d printed the vector we made
# print(c3dvec) # Here we 3d printed the vector we made


# class Animals:
#     animaltype = "mammals"

# class Pets:
#     color = "blonde"

# class Dogs:
#     @staticmethod
#     def bark():
#         print("bhau bhau")

# d = Dogs()
# d.bark()
                    #************ OR ************#
# class Animal:
#     animal = "cat"
# class Pet:
#     name = "birdie"
# class Cat:
#     @staticmethod
#     def meow():
#         print("Meow!!.........Meow!!")

# pet = Cat()
# pet.meow()




# class Employee():               # Here we created a class "Employee" 
#     salary = 4500000    # here we defiened salary in class employee
#     increment = 100000    # here we defiened increment in class employee  

#     @property               # Here we used the property decorator 
#     def salaryafterincrement(self):
#         return self.salary+self.increment       # This property decorator will return the salary after increment
    
#     @salaryafterincrement.setter                    # Here we defined a "setter method" which will return the increment according to the salary after increment we will define later
#     def salaryafterincrement(self,value):
#         self.increment = value-self.salary  # Here we defined the value of increment

# e1 = Employee()                 # Here we created an object "e1" under the class "Employee()" 

# print(e1.salaryafterincrement)      # Here we printed the salary after increment
# e1.salaryafterincrement = 7800000       # Here we defined or given a value to the total or the salary after increment
# print(e1.increment)     # Here we printed the increment
# print(e1.salary)        # Here we printed the salary




    