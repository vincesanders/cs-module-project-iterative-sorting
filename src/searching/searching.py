def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    middle = (len(arr) - 1) // 2
    while high - low > 0:
        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            low = middle
            middle = low + (high - low) // 2
        else: # target is smaller than arr[middle]
            high = middle
            middle = middle // 2
    return -1  # not found
