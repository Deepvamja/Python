arr = [1, 2, 3, 4, 5, 6, 7, 8]
d = 2
n = len(arr)
arr.reverse()

arr[:n-d] = arr[:n-d][::-1]
arr[n-d:] = arr[n-d:][::-1]
print(arr)


arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len(arr)

for i in range(d):
    arr.append(arr.pop(0)) 

print(arr)
