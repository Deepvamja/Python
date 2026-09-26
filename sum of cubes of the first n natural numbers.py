n = 5
res = ((n * (n + 1)) // 2) ** 2
print(res)


n = 5
sum = 0

for i in range(1, n + 1):
    res += i ** 3

print(res)


n = 5
res = sum([(i+1) ** 3 for i, _ in enumerate(range(n))])
print(res)
