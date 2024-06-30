import re
s = input("Enter pattern to check:")
m = re.fullmatch(s,"ababab")
if m!=None:
    print("full string matched")
else:
    print("full string is not matched")