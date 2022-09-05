class Flightdata:
    datatype = "Flightdata" 
    def printdata(self):
        print("applicant's name is",self.name)
        print(f"The name of flight is {self.flight}")       #Here we used f string to print the data

kartikeysapplication = Flightdata()
kartikeysapplication.name = "kartikey verma"
kartikeysapplication.flight = "Air India"
kartikeysapplication.printdata()


# class Railwaytickets:
#     datatype="raiway form"
#     def printdetails(self):
#         print(f"the name of pessanger is {self.name}")
#         print(f"the name of train is {self.train}")
    
# kartikeysapplication = Railwaytickets()
# kartikeysapplication.name = "KARTIKEY"
# kartikeysapplication.train = "rajdhani express"
# kartikeysapplication.printdetails()
