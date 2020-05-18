# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    while swapped:
        swaps = 0
        index = 0
        if index < len(arr) - 1: # if we're not at the last element
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
            # if no swaps, swapped is False 
            if swaps is 0:
                swapped = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
