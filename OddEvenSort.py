def oddEvenSort(arr, n):
    isSorted = 0
    while isSorted == 0:
        isSorted = 1

        # Odd phase
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0

        # Even phase
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0

arr = [34, 2, 10, -9]
n = len(arr)

oddEvenSort(arr, n)
print("Sorted array:", arr)
