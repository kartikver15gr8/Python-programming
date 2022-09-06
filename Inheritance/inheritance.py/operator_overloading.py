class Number():
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):     # This method is used for addition
        print("***Lets add***")
        return self.num + num2.num    
    
    def __mul__(self,num2):     # This method is used for multiplication
        print("***Lets multiply***")
        return self.num * num2.num

    def __sub__(self,num2):     # This method is used for subtraction
        print("***Lets subtract***")
        return self.num - num2.num

    def __truediv__(self,num2):     # This method is used for division
        print("***Lets divide***")
        return self.num / num2.num
    
    def __floordiv__(self,num2):        # This method is used for floordivision
        print("***Lets floordiv***")
        return self.num // num2.num  

n1 = Number(5)
n2 = Number(15)
sum = n1 + n2
mul = n1*n2
sub = n1-n2
div = n1/n2
floordiv = n1//n2

print(sum)
print(mul)
print(sub)
print(div)
print(floordiv)