// Using heapq.nlargest()

import heapq
l1 = [81, 52, 45, 10, 3, 2, 96]
print(heapq.nlargest(2, l1))


// Using sorted()

l = [2, 1, 8, 7, 3, 0, 9, 4]
n = 3

res = sorted(l, reverse=True)[:n]
print(res)


// Using numpy.argsort()

import numpy as np
l = [2, 6, 41, 85, 0, 3, 7, 6, 10]
n = 3
​
arr = np.array(l)
print(arr[np.argsort(arr)[-n:]])
