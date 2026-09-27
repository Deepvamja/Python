def stoogesort(arr, l, h):
    if l >= h:
        return

    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
    if h - l + 1 > 2:
        t = (h - l + 1) // 3

        stoogesort(arr, l, h - t)
        stoogesort(arr, l + t, h)
        stoogesort(arr, l, h - t)

arr = [2, 4, 5, 3, 1]
stoogesort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
