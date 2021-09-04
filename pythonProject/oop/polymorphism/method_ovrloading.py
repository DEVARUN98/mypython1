#polymorphism(many forms)
# #overloading     same method name,diff num of parameters(python ippol support cheyyunnilla)
# #overriding     same method name,same num of parameters
#
# class Person:
#     def show(self,num1):
#         self.num1=num1
#         print(self.num1)
# class Student(Person):
#     def show(self,num2,num3):   #method name same(show)
#         self.num2=num2
#         self.num3=num3
#         print(self.num2,self.num3)
# per=Student()
# per.show(3,0)   #2 arguments ulla show method aanenkil 2 arguments ullath work cheyyum
                #1 arguments ulla show method aanenkil 1 arguments ullath work cheyyanm.
                # but python latest create aaya method call cheyyum


# class Child:
#     def show(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Student(Child):
#     def show(self,mark):
#         self.mark=mark
#         print(self.mark)
# st=Student()
# st.show(1)      #st.show(2,1) kodthaal out kittilla..latest mathre execute cheyyoo





class Operator:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1,self.n2)
    def num(self,n3):
        self.n3=n3
        print(self.n3)
op=Operator()
op.num(1)