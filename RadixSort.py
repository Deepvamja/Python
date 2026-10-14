def radix_sort(arr):
    max_num = max(arr)
    exp = 1  # Represents current digit place (1, 10, 100, ...)

    while max_num // exp > 0:
        n = len(arr)
        output = [0] * n
        count = [0] * 10  # For digits 0–9

        # Count occurrences of each digit
        for num in arr:
            index = (num // exp) % 10
            count[index] += 1

        # Convert count[] to actual positions
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build output array (in reverse for stability)
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copy output to arr[]
        for i in range(n):
            arr[i] = output[i]

        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)
