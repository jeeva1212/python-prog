# we can pass pattern directly as argument to finditer()function:

import re
count = 0
matcher = re.finditer("ab","abaababa")
for match in matcher:
    count+= 1
    print(match.start(),"...",match.end(),"...",match.group())
print("the number of occurence:",count)