t = [(3, 4, 9), (5, 6, 7)]
tup = (1, 2, 5)
K =3
res = min(t, key=lambda x: abs(x[K-1] - tup[K-1]))
print(res)


import heapq

t = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
tup = (17, 23)
K = 2
res = heapq.nsmallest(1, t, key=lambda x: abs(x[K-1] - tup[K-1]))[0]
print(res)
