def gnomeSort(arr, n):
    ind = 0
    while ind < n:
        if ind == 0:
            ind += 1
        if arr[ind] >= arr[ind - 1]:
            ind += 1
        else:
            arr[ind], arr[ind - 1] = arr[ind - 1], arr[ind]
            ind -= 1
    return arr

arr = [34, 2, 10, -9]
n = len(arr)

arr = gnomeSort(arr, n)
print( *arr)
