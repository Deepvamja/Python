from collections import Counter
s = "GeeksforGeeks"
freq = Counter(s)
res = min(freq, key=freq.get)
print(str(res))




s = "GeeksforGeeks"
d = {}

for char in s:
    d[char] = d.get(char, 0) + 1 

sorted_freq = sorted(d.items(), key=lambda item: item[1])
res = sorted_freq[0][0]
print(res)
