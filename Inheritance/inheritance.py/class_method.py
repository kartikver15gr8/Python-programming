class Employee:
    company = "facebook"
    salary = 1000               # This is a class attribute salary

    # def changeSalary(self , sal): # This is an instance attribute to change salary but it will only add a new salary i will not change the class attribute salary at all
    #     self.salary= sal
    
    # def changeSalary(self , sal): # This is a method to also change the class arrtibute salary
    #     self.__class__.salary= sal
   
    @classmethod
    def changeSalary(cls,sal):      # By using using this class method we can also change the class attribute by assigning an instance attribute
        cls.salary=sal



e = Employee()
print(e.company)
print(e.salary)


e.changeSalary(2955)

print(e.salary)

print(Employee.salary)
