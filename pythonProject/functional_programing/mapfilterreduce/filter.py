#filter(function,iterable)

# lst=[1,2,4,7,8]
#
#
# # def check_even(num):
# #     return num%2==0
# #
# #
# # evens=list(filter(check_even,lst))
# # print(evens)
#
# #in lambda
# evens=list(filter(lambda num:num%2==0,lst))
# print(evens)
#
# odds=list(filter(lambda num:num%2!=0,lst))
# print(odds)


employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
# #developer_details
# developers=list(filter(lambda employee:employee["department"]=="developer",employees))
# print(developers)


#developer_name_only
developers=list(filter(lambda employee:employee["department"]=="developer",employees))
developer_name=list(map(lambda developer:developer["e_name"],developers))  #developers nte avde munpile linil type
                                                                    # cheytha condition type cheythaalum mathi
                                                                    #ith aaan first execute cheyyuka
print(developer_name)