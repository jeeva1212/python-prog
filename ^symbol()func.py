import re
s = "Learning python is very Easy"
res = re.search("^Learn",s)
if res!=None:
    print("Target string start with Learn")
else:
    print("Target string not starts with Learn")