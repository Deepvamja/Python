s = "101010000111"
if all(c in '01' for c in s):
    print("Yes")
else:
    print("No")

Using set()

s = "101010000111"
if set(s).issubset({'0', '1'}):
    print("Yes")
else:
    print("No")


s = "101010000111"
for char in s:
    if char not in '01':
        print("No")
        break
else:
    print("Yes")
