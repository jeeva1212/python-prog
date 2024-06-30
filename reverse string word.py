#reverse string in sorting type:

"""txt="dextris software solution"[::-1]
print(txt)"""

#reverse string in function type:

"""def my_function(x):
    return x[::-1]

my_txt = my_function("dextris software solution")
print(my_txt)"""

#reversestring:

def  reversestring(x):
    # Declaring an empty string
    Newstring = ""
    # Traversing through individual character in a string
    for i in x:
        # Add the character to the empty string
        Newstring = i + Newstring
      # return the new string
    return Newstring
# Sample string
Newstring = "dextris software solution"
 # Function call
Reversedstring = reversestring(Newstring)
# printing output
print(Reversedstring)

# input type reversed the string

'''def my_function(x):
    return x[::-1]

user_input = input("enter the string:")
my_txt = my_function(user_input)
print(my_txt)'''