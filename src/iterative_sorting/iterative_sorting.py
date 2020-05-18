# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        if smallest_index is not cur_index:
            smallest_value = arr[smallest_index]
            arr[smallest_index] = arr[cur_index]
            arr[cur_index] = smallest_value
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    index = 0
    swaps = 0
    last_element = len(arr) - 1
    while swapped:
        if index < last_element: # if we're not at the last element
            # compare item at index with index after
            if arr[index] > arr[index + 1]:
                # if item at index is larger, swap
                largerValue = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = largerValue
                # increment swaps
                swaps += 1
            #increment index
            index += 1
        else: # last index
            # decrement last element
            # we know the last element doesn't have to be checked again,
            # because we know it's the largest
            last_element -= 1
            # if no swaps, swapped is False 
            if swaps is 0:
                swapped = False
            else:
                index = 0
                swaps = 0
    return arr

#Space complexity of bubble and selection sort are O(n), time complexity is (O)n^2 / 2, which is further simplified to O(n)^2

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
