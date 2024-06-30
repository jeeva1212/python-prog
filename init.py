'''#To write a program to find number of occurences of each letter present
# in the given string:

word=input("enter any word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"occurred",v,"times")


n=int(input("Enter the number of students: "))
d={}
for i in range(n):
     name=input("Enter Student Name: ")
     marks=input("Enter Student Marks: ")
     d[name]=marks
while True:
     name=input("Enter Student Name to get Marks: ")
     marks=d.get(name,-1)
     if marks== -1:
         print("Student Not Found")
     else:
         print("The Marks of",name,"are",marks)
         option=input("Do you want to find another student marks[Yes|No]")
         if option=="No":
             break
print("Thanks for using our application")'''

'''def function(reverse):
    return reverse
s="thameem ansari"
s=s.split()[::-1]
x=s.reverse
print(s)'''


'''for i in range(0,11):
    print(i,"x2=",i*2)'''

'''def maximum(a,b):
    if a>=b:
        return a
    else:
        return b
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
print(maximum(a,b))'''

'''num = int(input("Enter a number:"))
factorial = 1
if num<0:
    print("Sorry,factorial does not exits negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)'''


'''class monkey:
    def patch(self):
        print("patch() is being called")

def monk_p(self):
    print("monk_p() is being called")
# Replacing address of "patch" with "monk_p"
monkey.patch = monk_p

obj = monkey()
obj. patch()
# monk_p() is being called'''

'''def organize_files(directory):
    # Define file type categories and their extensions
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.ppt', '.pptx']
    }

    # Create subfolders for each file type category if they do not exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to respective folders based on their extensions
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break
            if not moved:
                print(f"File {filename} does not match any known file type categories.")


# Example usage
directory = 'path_to_user_directory'  # Replace with the path to your directory
organize_files(directory)'''


'''# List comprehension

my_list = [i for i in range(1,10)]
print(my_list)
#[1,2,3,4,5,6,7,8,9]

# Dictionary comprehension

my_dict = {i for i in range(1,10)}
print(my_dict)
#{1,2,3,4,5,6,7,8,9}

# Tuple comprehension

my_tuple = (i for i in range (1,10))
print(my_tuple)
#<generator object<genexpr> at 0x7fb91b151430'''

'''# The __init__() in python:

class book_shop:
    # Constructor
    def __init__(self,title):
        self.title = title
    # Sample method
    def book(self):
        print("The title of the book is",self.title)
b = book_shop('sandman')
b.book()
# The title of the book is sandman'''

'''li=[-10,5,-3,8,4,2]  #o/p:14
max=0
out=[]
for i in range(len(li)):
    sum=0
    sum=sum+li[i]
    for j in range(i+1,len(li)):
        sum=sum+li[j]
        start=i
        end=j
    if sum>=max:
        out=[]
        max=sum
        out=out+li[start:end+1]
print(max)'''

'''s="java programming"
s=s[:13]+'e'+s[14:]
print(s)'''


