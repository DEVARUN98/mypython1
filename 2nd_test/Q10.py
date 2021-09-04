import re
x='[A-Z][a-z]+'
n=input("enter the string")
matcher=re.fullmatch(x,n)
if matcher!=None:
    print("Valid")
else:
    print("Invalid")