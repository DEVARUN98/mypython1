#function use cheyth aaan decorator create cheyyunnath
#function ne control cheyyaan
#oru function nte ullil vere oru function create cheythittan decorator undakkunnath
#oru decorator il ethra function venamenkilm use cheyyaaam


# def revert_val(func):       #div(2,10)
#     def wrapper(no1,no2):   #wrapper common name, name can change,but no.of parameter same
#         if no1<no2:
#             (no1,no2)=(no2,no1)
#             return func(no1,no2)     #div(10,2)
#         else:
#             return func(no1,no2)
#     return  wrapper    #wrapper function work cheyynamenkil return use cheyyanm
#
#
# @revert_val
# def sub(num1,num2):
#     return num1-num2
# print(sub(3,10))
#
# @revert_val
# def div(num1,num2):
#     return num1/num2
# print(div(2,10))










def admin_required(func):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("You are not allowed")
        else:
            return func(a,b)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_ac(user,acno):
    return str(acno)+" delete"

print(change_pin("admin",1000))
print(delete_ac('admin',1000))














# def covid_vaccine(func):
#     def wrapper(a,b,c):
#         if a<18:
#             raise Exception("you are not eligiblle")
#         else:
#             return func(a,b,c)
#     return wrapper
#
# @covid_vaccine
# def covid(age,name,place):
#     age=age
#     name=name
#     place=place
#     return name+" from "+place+" eligible"
# print(covid(18,'anu','malappuram'))
