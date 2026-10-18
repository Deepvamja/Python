arr = [100, 10, 5, 25, 35, 14]
n = 11
mul = 1
for num in arr:
    mul = (mul * (num % n)) % n

print(mul)
