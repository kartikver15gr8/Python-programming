#Q1
# class Progrsammer():
#     company = "Microsoft"
#     def __init__(self,name,id,workplace):
#         self.name = name 
#         self.id = id
#         self.workplace = workplace
#     def printData(self):
#         print(f"The name of the employee working in MICROSOFT is :{self.name}")
#         print(f"The id of that employee is :{self.id}")
#         print(f"And the workplace of that employee  is :{self.workplace}")

# kartik = Progrsammer("kartik", "0901MS457898", "Banglore")
# rajiv = Progrsammer("rajiv", "0901MS457899", "Banglore" )

# kartik.printData()
# rajiv.printData()

#Q2

# class Calculator:
#     def __init__(self,num):
#         self.number
#     def square(self):
#         print(f"the square of {self.num} is {self.num**2}")
#     def square_root(self):
#         print(f"The value of square_root of {self.num} is {self.num**0.5}")
#     def cube(self):
#         print(f"The value of cube of {self.num} is {self.num**3}")
        
# a = Calculator(5)
# a.square()
# a.square_root()
# a.cube()

#***************************** OR ****************************


# class calculator():
#     def __init__(self,num):
#         self.number = num
#     def square(self):
#         print(f"the square of {self.number} is {self.number**2} ")
#     def cube(self):
#         print(f"the cube of {self.number} is {self.number**3}")       
#     def squareroot(self):
#         print(f"the squareroot of {self.number} is {self.number**0.5}")

# a = calculator(5)
# a.squareroot()
# a.cube()
# a.square()

#Q3
# class sample():
#     a = "captain america"

# obj = sample()
# sample.a = "HULK"   # here we changed the class attribute by making an instantaneous attribute with the same name
# obj.a = "thor"      # by creating this instance object attribute the initial class attribute a will not change
# print(obj.a)
# print(sample.a)

#Q4

# class calculator():
#     def __init__(self,num):
#         self.number = num
#     def square(self):
#         print(f"the square of {self.number} is {self.number**2} ")
#     def cube(self):
#         print(f"the cube of {self.number} is {self.number**3}")       
#     def squareroot(self):
#         print(f"the squareroot of {self.number} is {self.number**0.5}")
#     @staticmethod
#     def greet():
#         print("hello")

# a = calculator(5)
# a.squareroot()
# a.cube()
# a.square()
# a.greet()

#Q5

# class Train():
#     def __init__(self,name,fare,netfare,seats):
#         self.name = name 
#         self.fare = fare
#         self.seats = seats
#         self.netfare = netfare
#     def getStatus(self):
#         print(f"the name of train is {self.name}")
#         print(f"the netfare of reservation in train is {self.netfare}")
#         print(f"the seats reserved in train is {self.seats}")

#     def getFareinfo(self):
#         print(f"the fare of the ticket in this train is {self.fare}")

#     def bookTickets(self):
#         if(self.seats>0):
#             print("the seats are available in the train now you may book the tickets in the train ")
#         else:
#             print("So sorry all the seats in this train are already reserved")


# Garibrath = Train("Garibrath express 10015","Rs 750/-","Rs 3400/-",4)
# Garibrath.getFareinfo()
# Garibrath.getStatus()
# Garibrath.bookTickets()

# class Calculator():

#     def __init__(self,num):
#         self.number = num
#     def square(self):
#         print(f"the square of {self.number} is {self.number**2}")
#     def cube(self):
#         print(f"the cube of {self.number} is {self.number**3}")
#     def squareroot(self):
#         print(f"the squareroot of {self.number} is {self.number**0.5}")
    

# a = Calculator(10)
# a.square()
# a.cube()
# a.squareroot()








