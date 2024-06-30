import re
matcher = re.finditer("\S","a7b k@9z")
for match in matcher:
    print(match.start(),"...",match.group())