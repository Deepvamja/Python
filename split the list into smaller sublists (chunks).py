a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3 
res = [a[i:i + n] for i in range(0, len(a), n)]
print(res) 



// Using itertools.islice


from itertools import islice
a = [1, 2, 3, 4, 5, 6, 7, 8]  
n = 3  

it = iter(a) 
res = [list(islice(it, n)) for _ in range((len(a) + n - 1) // n)]
print(res)
