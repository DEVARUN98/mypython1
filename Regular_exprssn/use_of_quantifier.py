import reg

x='a+'    #a including roup
r="aaa abc aaaa cga"
matcher=reg.finditer(x, r)
for match in matcher:
    print(match.start())
    print(match.group())
