# create the set function

a={10,20,10,30,40,10}
s=set(a)
print(s)

# how find the set range

s=set(range(5))
print(s)

#add to set func

s={10,20,30}
s.add(40,)
print(s)

#update (x,y,z) set func:

s={10,20,30}
i={40,50,60,70,80}
s.update(i)
print(s)

s={10,20,30}
i={40,50,60,70,80}
s.update(i,range(5))
print(s)

# pop func in set

s={40,10,30,20}
print(s)
print(s.pop())
print(s)


s={10,30,20}
print(s)
print(s.pop())
print(s)

#membership operator :(in,not in)

s=set("anjana")
print(s)
print("a" in s)
print("e" in s)

#set comprehension:

s = {2 ** x for x in range(2, 10, 2)}
print(s)



#data structure in dictionary

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


    # pop in dict func:

    d = {100: "durga", 200: "ravi", 300: "shiva"}
    print(d.pop(100))
    print(d)
    print(d.pop(400))


#sum of values in dictionary:

d=eval(input("Enter dictionary:"))
s=sum(d.values())
print("Sum= ",s)


#To write a program to find number of occurences of each letter present
# in the given string:

word=input("enter any word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"occurred",v,"times")

    # dictionary comprehensiom

    squares = {x: x * x for x in range(1, 6)}
    print(squares)
    doubles = {x: 2 * x for x in range(1, 6)}
    print(doubles)