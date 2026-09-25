from collections import Counter
s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"

count = Counter(s1.split()) + Counter(s2.split())
res = [word for word in count if count[word] == 1]
print(res)
