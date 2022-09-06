
class Amit():
    identity = "person"
    def amitBhai(self):
        print("hnji hm hi hai amit bhai")
class Rahul(Amit):
    age = "21"
    def rahulAge(self):
        print("bataya toh bhai rahul 21 saal ka hai")
        super().amitBhai()
    def amitBhai(self):
        print("amit bhai")

class Hmm(Rahul):
    def kholDo(self):
        print("hnji bhaiya kesa laga yeh example to show multilevel inheriance")
    def amitBhai(self):
        print("amit")

a = Amit()
b = Rahul()
c = Hmm()

a.amitBhai()
b.amitBhai()
b.rahulAge()
c.amitBhai()
c.kholDo()
c.rahulAge()
c.amitBhai()
