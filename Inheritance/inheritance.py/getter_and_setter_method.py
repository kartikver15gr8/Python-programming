class Employee():       # Here we defined a class Employee
    company = "java"    
    salary = 9500
    salarybonus = 1500

    @property             # This is our property decorator or getter method in python
    def totalSalary(self):  # In this getter method or property decorator we defined a function i.e totalSalary
        return self.salary + self.salarybonus  # This will return the total salary be adding the salary bonus and salary


    @totalSalary.setter     # This is our setter method in python this method can be implemented to get a basic abstraction 
    def totalSalary(self,value):  # Here in this setter method we defined a function total salary
        self.salarybonus = value-self.salary   # This will return the salary bonus by subtracting the salary from our defined total salary
        
e = Employee()     # Here we created an object in class Employee
print(e.totalSalary)  # Here the total salary get printed by our property decortor
e.totalSalary = 25000  # here we defined the total salary as 15000
print(e.salary)  
print(e.salarybonus)        # Here the salary bonus gets printed by the setter method we have made above in the program