import re
s = "Learning python is very Easy"
res = re.search("easy$",s,re.IGNORECASE)
if res!=None:
    print("Target string ends with Easy by ignoring case")
else:
    print("Target string not ends with Easy by ignoring case")
