#tuples modify in index value

t=(1,2,3,4,5,6)
print("original tuple",t)
l =list(t)   #change tuple to list
l[2]=100     #update a value
t=tuple(l)   #converting it back to tuple
print("update tuple",t)
print(type(t))

#slicing in tuple

t=(1,2,3,4,5,6)
print("original tuple",t)
#slicing

t=t[:2]+(100,)+t[3:]
print("update tuple",t)

#modify to index position

t = (1, 2, 3, 4, 5, 6, 7, 8)
print("Original tuple", t)

i = 4 #index position
t = (*t[:i], '300', *t[i+1:]) # update the value 300 at index position 4
print("Updated tuple", t)

#modifying in tuple

t = tuple("ABCDEFGHIJKLMN0")
print("Original tuple", t)

i = (len(t)//2) #index position
t = (*t[:i], '1000', *t[i+1:]) # update the value 300 at index position 4
print("Updated tuple", t)

tuple1 = (1,2,3,4,5,6,7)
list1 = list(tuple1)
list1[5] = 9
tuple1 = tuple(list1)
print(tuple1)