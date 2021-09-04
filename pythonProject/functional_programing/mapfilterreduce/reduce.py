# from functools import reduce   #reduce ne  import cheyyaan
#
# lst=[1,3,2,5,7]
# sum=reduce(lambda num1,num2:num1+num2,lst)
# print(sum)


# num1=23
# num2=13
# # if(num1>num2):
# #     print(num1)
# # else:
# #     print(num2)
# print(num1 if num1>num2 else num2)


# num1=int(input("ente a number"))
# if(num1<0):
#     print("-ve")
# else:
#     print("+ve")
#
# print("negative" if num1<0 else "positive")

from functools import reduce
lst=[2,3,6,4]
largest=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(largest)





#cases
#1 iterable value  must be integers