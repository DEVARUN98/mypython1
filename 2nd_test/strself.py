# used in two string method
# used two print a common attribute value in a program
# Mainly  available for string type values. Integer values need to convert into string for further operations
# Return keyword is used and '+'  is used if two values need to print


class child:
    def __init__(self,name,age,clas,school):
        self.name=name
        self.age=age
        self.clas=clas
        self.school=school
    def printv(self):
        print(self.name,self.age,self.clas,self.school)
    def __str__(self):
        return self.clas+str(self.school)
chi=child('manu',20,12,'abc')
chi.printv()
print(chi)
