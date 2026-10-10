def shell_ciura(a):
    n = len(a)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for g in gaps:
        if g >= n: 
            continue
        for i in range(g, n):
            t = a[i]
            j = i
            while j >= g and a[j-g] > t:
                a[j] = a[j-g]
                j -= g
            a[j] = t

arr = [12, 34, 54, 2, 3]
shell_ciura(arr)
print(arr)
