# example 1

class Employee():
    company = "java"
    salary = 9500
    salarybonus = 1500

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

e = Employee()
print(e.totalSalary)

# example 2

# class Loan():
#     loan = 250000
#     monthly_interest = 900
#     emi = 1500
#     total_installment = monthly_interest+emi

#     @property
#     def netEmi(self):
#         return self.monthly_interest+self.emi

# payer = Loan()
# print("the monthly interest paid by the payer is: ")
# print(payer.total_installment)