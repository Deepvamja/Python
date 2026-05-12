import numpy as np
lst = [["Deep", "good"], ["is", "for"], ["Best"]]

m = max(len(x) for x in lst)
p = [x + [''] * (m - len(x)) for x in lst]

arr = np.array(p).T
res = [''.join(r) for r in arr]
print(str(res))