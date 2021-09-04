class Sudent:
    def __init__(self,name,rollno,department,mark):
        self.name=name
        self.rollno=rollno
        self.department=department
        self.mark=mark
    def printval(self):
        print("name=",name)
        print("rollno=",rollno)
        print("department=",department)
        print("mark=",mark)
    def __str__(self):
        return self.name



f=open('wrk.txt', 'r')
for line in f:
    data=line.split(",")
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=int(data[3])
    obj=Student(name,rollno,course,mark)
    print(obj)
    obj.printval()