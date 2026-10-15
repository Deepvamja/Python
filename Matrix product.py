import numpy as np
a = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

b = [ele for sub in a for ele in sub]  
res = np.prod(b)
print(res)
