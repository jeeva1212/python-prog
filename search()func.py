import re
s = input("Enter pattern to check:")
m = re.search(s,"abaaaba")
if m!=None:
    print("match is available")
    print("first occurrence of match with start index:",m.start(),"and end index:",m.end())
else:
    print("match is not available")