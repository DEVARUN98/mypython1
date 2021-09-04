import re
x='[A-Z]+[a-zA-Z0-9]{3-8}[A-Z]$'
n=input("Enter the string:")
matcher=re.fullmatch(x,n)
if matcher!=None:
    print("Valid")
else:
    print("Invalid")