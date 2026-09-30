def combSort(arr):
    n = len(arr)
    gap = n
    swapped = True
    
    def getNextGap(gap):
        gap = int((gap * 10) / 13)
        return 1 if gap < 1 else gap
    
    while gap != 1 or swapped:
        gap = getNextGap(gap)
        swapped = False

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

arr = [8, 4, 1, 3, -44, 23, -6, 28, 0]
combSort(arr)

print(*arr)
