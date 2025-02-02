
#ascending_order
nums = [5, 7, 8, 4, 1, 6, 9, 2]

def selection_sort(nums):
    N = len(nums)
    for i in range(0,N):  # Loop through each element
        min_index = i
        for j in range(i + 1, N):  # Find the smallest element in the remaining array
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]  # Swap the elements

selection_sort(nums)
print(nums)  # Output the sorted list


#descending order
nums = [5, 7, 8, 4, 1, 6, 9, 2]

def selection_sort(nums):
    N = len(nums)
    for j in range(0,N):  # Loop through each element
        max_index = j
        for i in range(j + 1, N):  # Find the smallest element in the remaining array
            if nums[i] > nums[max_index]:
                max_index = i
        nums[j], nums[max_index] = nums[max_index], nums[j]  # Swap the elements

selection_sort(nums)
print(nums)





