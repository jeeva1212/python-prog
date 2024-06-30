import re
s = input("Enter pattern to check:")
m = re.match(s,"abcabdefg")
if m!=None:
    print("match is available at the beginning of the string")
    print("start index:",m.start(),"add end index:",m.end())
else:
    print("match is not available at the beginning of the string")
