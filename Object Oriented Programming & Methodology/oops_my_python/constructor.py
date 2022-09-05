# class Employee:
#     company = "Google"

#     def __init__(self):
#         print("employee is created")
        
        

#     def getSalary(self):
#         print("salary is 1000k")

# kartik = Employee()
# kartik.getSalary()

class Employee:
    company = "Google"
    def __init__(self,name,salary,division):
        self.name = name
        self.salary = "54,00,000/-"
        self.division = division
    def getDetails(self):
        print(f"The division of the employee is {self.division}")
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        
    # def getSalary(self):
    #     print("salary is 1000k")

kartik = Employee("kartik","54,00,000/-","Data scientist")
# kartik.getSalary()
kartik.getDetails()
