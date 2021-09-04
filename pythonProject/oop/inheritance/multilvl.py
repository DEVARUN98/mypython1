# #also named as hierarchical inheritance
# # class A:
# #     def printA(self):
# #         print("inside A")
# # class B(A):
# #     def printB(self):
# #         print("inside B")
# # class C(B):
# #     def printC(self):
# #         print("inside C")
# # a=A()
# # a.printA()
# # b=B()
# # b.printB()
# # b.printA()
# #
# # c=C()
# # c.printC()
# # c.printB()
# # c.printA()
#






#
# class Person:
#     def set(self,name,age,adrs):
#         self.name=name
#         self.age=age
#         self.adrs=adrs
#         print(self.name,self.age,self.adrs)
# class Child(Person):
#     def setv(self,school,std):
#         self.school=school
#         self.std=std
#         print(self.school,self.std)
# class Student(Child):
#     def printv(self,rollno,mark):
#         self.rollno=rollno
#         self.mark=mark
#         print(self.rollno,self.mark)
#
# st=Student()
# st.set('anu',23,'abc')
# st.setv('ab',3)
# st.printv(22,13)



class Person:
    def set(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)

class Child(Person):
    def setv(self,clas,school):
        self.clas=clas
        self.school=school
        print(self.clas,self.school)
#
class Parent(Person):
    def setvv(self,job,company):
        self.job=job
        self.company=company
        print(self.job,self.company)

class Student(Child):
    def printv(self,mark,rollno):
        self.mark=mark       # Student class nte parent class Child and Person aaan
        self.rollno=rollno
        print(self.mark,self.rollno)

st=Student()
st.set('anu',22)
st.setv(12,'abc')
pr=Parent()
pr.setvv('engg','abcsd')
st.printv(23,12)



                #CONSTRUCTOR IN INHERITANCE
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
#     def printval(self):
#         print("Name=",self.name)
#         print("Age=", self.age)
#
# class Student(Person):
#     def __init__(self,rollno,mark,name,age):  #Child class parent class ne inherit cheyyunnath kondan name,age add cheythath
#         super().__init__(name,age)     #Person nte attributes ne call cheyyaan vendi
#         self.rollno=rollno
#         self.mark=mark
#     def print(self):
#         print("Rollno=",self.rollno)
#         print("Mark=",self.mark)
# cr=Student(2,43,'anu',23)
# cr.printval()
# cr.print()

# anu 23
# Name= anu
# Age= 23
# Rollno= 2
# Mark= 43
# anu1
# 1 CS anu abc





# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printVal(self):
#         print("Name=",self.name)
#         print("Age=", self.age)
# class Employee(Person):
#     def __init__(self,company,salary,name,age):
#         super().__init__(name,age)
#         self.company=company
#         self.salary=salary
#     def printv(self):
#         print(self.company)
#         print(self.salary)
# em=Employee('abc',50000,'anu',23)
# em.printVal()
# em.printv()


                       #TWO STRING METHOD
class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color
    def printv(self):
        print(self.model,self.regno,self.color)
    def __str__(self):
        return self.model+self.color       #model common aayi kodkkaan vendi(string mathram kodukkavoo , oru value mathram return kodukkavoo)
        # 2 values kodkkaan vendi use + instead ,. Concatenate cheyth one value aayttan return cheyyunnath
ve=Vehicle('RE','KL10BE8617','black')
ve.printv()
print(ve)





# class Student:
#     def __init__(self,name,rollno,dept):
#         self.name=name
#         self.rollno=rollno
#         self.dept=dept
#      #   self.college=college
#     def printv(self):
#         print(self.name,self.rollno,self.dept)
#     def __str__(self):
#        # return self.name+self.dept
#         return self.name+str(self.rollno)  # str() kodthirikkunnath string aakki output kittan vendiyaan
# st=Student('anu',12,'cse')
# st.printv()
# print(st)





# parent,teacher
class Parent:
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
    def printv(self):
        print(self.name,self.addr)
class Teacher(Parent):
    def __init__(self,id,dept,name,addr):
        super().__init__(name,addr)
        self.id=id
        self.dept=dept
    def printvv(self):
        print(self.id,self.dept,self.name,self.addr)
    def __str__(self):
        return self.name+str(self.id)
te=Teacher(1,'CS','anu','abc')
print(te)
te.printvv()

