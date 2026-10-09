import pandas as pd
t1 = [["Gfg", "good"], ["is", "for"], ["Best"]]
df = pd.DataFrame(t1)
res = df.fillna('').apply(''.join)
print(list(res))



import numpy as np
lst = [["Gfg", "good"], ["is", "for"], ["Best"]]

m = max(len(x) for x in lst)
p = [x + [''] * (m - len(x)) for x in lst]

arr = np.array(p).T
res = [''.join(r) for r in arr]
print(str(res))
