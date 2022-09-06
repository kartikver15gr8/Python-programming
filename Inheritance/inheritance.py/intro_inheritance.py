#************* this is an example of single inheritance ***********************

class Employee():           # Here we created a class named as "Employee"
    
    company = "Google"
    def printData(self):                # We defined a function in this class 
        print("this is an employee ")
class Programmer(Employee):         # Here we created a children class "Programmer" which will show inheritance from Employee
    def showData(self):     # We definede some functions in it
        print("this is a programmer working in Google")
    def tuTu(self):
        print("hey tutu")
    def printData(self):                # Here we updated the defined function of Employee
        print("i'm working honestly and hard")

kartik = Employee()             # Here we created an object in employee class
wayne = Programmer()            # Here we created an object in programmer class which will also inherit the defined functions in Employee class

print(kartik.company)
kartik.printData()
wayne.printData()
wayne.showData()
wayne.tuTu()

