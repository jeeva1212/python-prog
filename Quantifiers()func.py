#quantifiers:

import re
matcher=re.finditer("a*","abaabaaab")
for match in matcher:
    print(match.start(),"...",match.group())

