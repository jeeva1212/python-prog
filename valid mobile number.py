import re
n = input("Enter number:")
m = re.fullmatch("[7-9]\d{9}",n)
if m!=None:
    print("valid mobile number")
else:
    print("invalid mobile number")