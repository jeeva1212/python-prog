# Python3 code to alternatively merge two strings

# Function for alternatively merging two strings
def merge(s1, s2):
    # To store the final string
    result = ""

    # For every index in the strings
    i = 0
    while (i < len(s1)) or (i < len(s2)):

        # First choose the ith character of the
        # first string if it exists
        if (i < len(s1)):
            result += s1[i]

        # Then choose the ith character of the
        # second string if it exists
        if (i < len(s2)):
            result += s2[i]

        i += 1

    return result


# Driver Code
s1 = "ravi"
s2 = "teja"

print(merge(s1, s2))




"""def solve(s, t):
   i = j = 0
   result = ""
   while i < len(s) and j < len(t):
      result += s[i] + t[j]
      i+=1
      j+=1
   while i < len(s):
      result += s[i]
      i += 1
   while j < len(t):
      result += t[j]
      j += 1
   return result
s = "ravi"
t = "teja"
print(solve(s, t))"""