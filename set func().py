#name and percentage marks in dict:

rec={}
n=int(input("Enter number of students: "))
i=1
while i <=n:
     name=input("Enter Student Name: ")
     marks=input("Enter % of Marks of Student: ")
     rec[name]=marks
     i=i+1
print("Name of Student","\t","% of marks")
for x in rec:
    print("\t",x,"\t\t",rec[x])

    # Add phone no in dict func()

    name = {"name": "ansari", "color": "white", "d.o.b": 2001}
    name["phone"] = 8098091970
    print(name)