#pattern matching
# re - package for pattern matching
# import re - import cheyyaan vendi
#finditer -method in regular exprssn
#group() -which object find match
#package nte ullil niinn fuction ne call cheyyumbol function name use cheyth call cheyyanm


import reg
count=0
matcher=reg.finditer('ab', 'abaabbab')
for match in matcher:
    count+=1
print("count=",count)





# x='[abc]'    either a b or c
# x='[^abc]'    except abc
# x='[a-z]'    a to z
# x='[A-Z]'     A to Z
# x='[a-zA-Z]'    both lower and upper
# x='[0-9]'     check digits
# x='[a-zA-Z0-9]'     special symbols
# x='\s'      check space
# x='\d'      check the digits
# x='\D'      except digits
# x='\w'      all words except special character
# x='\W'      for special character


#QUANTIFIERS-condition kodkkaan vendi.ethra tym execute cheyyanam ennariyaan
# x='a+'    a incuding group
# x='a*'    count including zero number of a
# x='a?'   count a as each including zero no. of a
# x='a{2}'       2 a's
# x='a{2,3}'   minimum two a  and maximum three
# x='^a'     to check whether starting with a or not
# x='a$'      check ending with a

import reg
count=0
matcher=reg.finditer('ab', 'abaabbab')
for match in matcher:
    print("match available at",match.start())      #return position
    print("group=",match.group())                #which object find match
    count+=1
print("count=",count)