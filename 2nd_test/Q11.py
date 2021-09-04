import re

x='^a[0-9]+b$'
n=input("enter the string")
matcher=re.fullmatch(x,n)
if matcher!=None:
    print("Valid")
else:
    print("Invalid")