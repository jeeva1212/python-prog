import re
t = re.subn("[a-z]","#","a7b9c5k8z")
print(t)
print("The Result string:",t[0])
print("The number of replacements:",t[1])
