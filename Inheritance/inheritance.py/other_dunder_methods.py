class Number():
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):     # This method is used for addition
        print("***Lets add***")
        return self.num + num2.num    

    def __str__(self):      # This is the dunder method "str"
        return f"This is a decimal number {self.num}"

    def __len__(self):      # This is the len dunder method of python
        return 1


n = Number(10)
print(n)
print(len(n))