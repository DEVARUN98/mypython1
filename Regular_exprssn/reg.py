# import re
# x='[abc]'
# matcher=re.finditer(x,'abc 978@ckAzabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())




# import re
# x='[^abc]'
# matcher=re.finditer(x,'abc 978@ckAzabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())



# import re
# x='[0-9]'
# matcher=re.finditer(x,'abc 978@ckAzabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())



# import re
# x='[a-z]'
# matcher=re.finditer(x,'abc 978@ckAzabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x='[A-Z]'
# matcher=re.finditer(x,'abc 978@ckAzabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())




# import re
# x='[a-zA-Z]'
# matcher=re.finditer(x, 'abc 978@ckAzabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
#
#
# import re
# x='[^0-9a-zA-Z]'
# matcher=re.finditer(x, 'abc 978@ckAzabc')   #index position vechaan count cheyyunnath.so 0 thottaaan starting
# for match in matcher:
#     print(match.start())
#     print(match.group())



# import re
# x="\w"
# matcher=re.finditer(x, 'abc 978@ckAzabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())



import re
x="\d"
matcher=re.finditer(x, 'abc 978@ckAzabc')
for match in matcher:
    print(match.start())
    print(match.group())

