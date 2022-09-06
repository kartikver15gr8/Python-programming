# Single inheritance
# class Employee():           # Here we created a class named as "Employee"
    
#     company = "Google"
#     def printData(self):                # We defined a function in this class 
#         print("this is an employee ")
# class Programmer(Employee):         # Here we created a children class "Programmer" which will show inheritance from Employee
#     def showData(self):     # We definede some functions in it
#         print("this is a programmer working in Google")
#     def tuTu(self):
#         print("hey tutu")
#     def printData(self):                # Here we updated the defined function of Employee
#         print("i'm working honestly and hard")

# kartik = Employee()             # Here we created an object in employee class
# wayne = Programmer()            # Here we created an object in programmer class which will also inherit the defined functions in Employee class

# print(kartik.company)
# kartik.printData()
# wayne.printData()
# wayne.showData()
# wayne.tuTu()





# Multiple inheritance
# class Employee():               # Here we created a class Employee
#     company = "josh"            
#     def showDetails(self):      # We defined a function in class employee
#         print("how's the day")
# class dataCharm():              # We created another class dataCharm
#     work = "Database management"
#     def printData(self):        # We defined a function in class dataCharm
#         print("doing great")
# class piCharm(Employee,dataCharm):      # Here we created a class which inherits from classes "Employee and dataCharm"
#     company = "Python"                  # This class piCharm will show multiple inheritance from classes "Employee and dataCharm"
#     def charMiss(self):
#         print("great!!")

# a = Employee()
# b = dataCharm()
# c = piCharm()

# c.printData()          # Here we are calling the function of the parent class and that's how its showing multiple inheritance                 
# c.showDetails()        # Here we are calling the function of the parent class and that's how its showing multiple inheritance     
# c.charMiss()


# Multilevel inheritance
# class Amit():
#     identity = "person"
#     def amitBhai(self):
#         print("hnji hm hi hai amit bhai")
# class Rahul(Amit):
#     age = "21"
#     def rahulAge(self):
#         print("bataya toh bhai rahul 21 saal ka hai")

# class Hmm(Rahul):
#     def kholDo(self):
#         print("hnji bhaiya kesa laga yeh example to show multilevel inheriance")

# a = Amit()
# b = Rahul()
# c = Hmm()

# a.amitBhai()
# b.amitBhai()
# b.rahulAge()
# c.amitBhai()
# c.kholDo()
# c.rahulAge()
