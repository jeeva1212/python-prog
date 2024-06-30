import re
s = "Learning python is Easy"
res = re.search("Easy$",s)
if res!=None:
    print("Target string ends with Easy")
else:
    print("Target string not ends with Easy")