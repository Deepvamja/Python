s = "101010000111"
if all(c in '01' for c in s):
    print("Yes")
else:
    print("No")



import re
s = "101010000111"
if re.fullmatch('[01]+', s):
    print("Yes")
else:
    print("No")
