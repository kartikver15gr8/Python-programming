class Employee:
    company = "Google"
    def getSalary(self):
        print("salary is 1000k")
        
    @staticmethod       # if we want to run the below defined funcion without using self so we can do that by this "static method"
    def greet():
        print("Good morning sir")

kartik = Employee()
kartik.getSalary()      # This will be interpreted as Employee.getSalary(kartik) just because we used self while defining the getSalary function 
kartik.greet()