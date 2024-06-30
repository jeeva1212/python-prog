def print_odd_even_char(string):
    odd_char=""
    even_char=""

    for i in range(len(string)):
          if i % 2 == 0:
              even_char += string[i]
          else:
              odd_char += string[i]
    print("enter the even:", even_char)
    print("enter the odd:", odd_char)
input_string = "Ansari"
print_odd_even_char(input_string)
