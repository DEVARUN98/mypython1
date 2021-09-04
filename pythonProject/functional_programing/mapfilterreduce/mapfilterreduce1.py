
lst=[2,3,4,5,6]
#squares of all numbers map

#map(function,list/iterables)


# def squares(num):
#     return num**2
# square=list(map(squares,lst))
# print(square)

#using_lambda_function
cubes=list(map(lambda num:num**3,lst))
print(cubes)
squares=list(map(lambda num:num**2,lst))
print(squares)