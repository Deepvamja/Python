arr = [[4, 5, 6, 8],
       [1, 2, 3, 1],
       [7, 8, 9, 4],
       [1, 8, 7, 5]]

n = len(arr[0])

# Print first row
for j in range(n):
    print(arr[0][j], end=" ")

# Print opposite diagonal
for i in range(1, n - 1):
    print(arr[i][n - i - 1], end=" ")

# Print last row
for j in range(n):
    print(arr[n - 1][j], end=" ")
