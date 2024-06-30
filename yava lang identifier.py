import re
s = input("Enter identifier:")
m = re.fullmatch("[a-k][0369][a-zA-Z0-9#]*",s)
if m!=None:
    print(s,"is valid yava identifier")
else:
    print(s,"is invalid yava identifier")
    