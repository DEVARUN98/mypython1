# #overloading     same method name,diff num of arguments(python ippol support cheyyunnilla)
# #overriding     same method name,same num of arguments

class Person:
    def printval(self,name):
        self.name=name
        print("inside person method",self.name)
class Child(Person):
    def printval(self,class1):
        self.class1=class1
        print("inside child method",self.class1)
ch=Child()
ch.printval('abc')

#child class method override person class method(latest aayttulla class call cheyyum)