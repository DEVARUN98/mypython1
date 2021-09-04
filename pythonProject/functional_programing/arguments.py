      #use of *args
#out of *args in tuple

# def printval(*args):
#     return args
# print(printval(2,3,4,5,6,7))   #ethra arguments venaamenkilm kodkkaam


        #**args
# kodukkunna data kk korachhooode clarity kodukkaan
# def printval(**args):
#     return args
# print(printval(name='anu',age='22',place='kochi'))
# #out of **args is dictionary



def printval(*args):
    sum=0
    for i in args:
        sum+=i
    return(sum)
print(printval(5,6,7,8,9,0))
# for i in args:
#     sum+=i
# print(printval())