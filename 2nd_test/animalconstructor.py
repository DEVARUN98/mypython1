class Animal:
    def __init__(self,name):
        self.name=name
        print(self.name)
    def printval(self):
        print("name=",self.name)
class Dog(Animal):
    def __init__(self,breed,name):
        super().__init__(name)
        self.breed=breed
        print(self.breed)
    def printv(self):
        print("breed=",self.breed)
dg=Dog('lab','rocky')
dg.printval()
dg.printv()
