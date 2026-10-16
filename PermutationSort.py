import random

def bogo_sort(arr):
    while True:
        sorted_flag = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sorted_flag = False
                break
        
        if sorted_flag:
            break  

        n = len(arr)
        for i in range(n):
            r = random.randint(0, n - 1)
            arr[i], arr[r] = arr[r], arr[i]

arr = [3, 2, 4, 1, 0, 5]
bogo_sort(arr)
print("Sorted array:", *arr)
