# #relate noun
# # display_value()   -snake notation   python
# # displayValue()    -camel notation  java  javascript
#
#
employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
## printing_salaries
# salaries=list(map(lambda employee:employee["salary"],employees))
# print(salaries)

##max_salary
# salaries=max(map(lambda employee:employee["salary"],employees))
# print(salaries)

##min_salary
salaries=min(map(lambda employee:employee["salary"],employees))
print(salaries)


##printing_employee_name
# e_name=list(map(lambda employee:employee["e_name"],employees))
# print(e_name)
#
# for employee in employees:
#     print(employee["e_name"])

##converting_to_upper
# e_upper=list(map(lambda employee:employee["e_name"].upper(),employees))
# print(e_upper)       #using map and lambda
# for employee in employees:
#     print(employee["e_name"].upper())

# # print employee name who are workn as dvlper
# for employee in employees:
#     if(employee["department"]=="developer"):
#         print("developer",employee["e_name"])
#
# #total_of_salary
# total=0
# for employee in employees:
#     total+=employee["salary"]
# print(total)
#
# #1 case map
# #2 case filter
# #2 case reduce
#
#
# #print_employee_names_name_starting_with-"a"    filter
# #print lowest salary reduce
# #














