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
def count_sort(arr, maximum=-1): # currently O(4n+k)
    # find k(maximum) while creating sorted_array
    sorted_array = []
    for i in range(len(arr)): # O(n)
        sorted_array.append(0)
        if arr[i] > maximum:
            maximum = arr[i]
        elif arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
    # make count array with values of 0
    count = [0 for x in range(maximum + 1)]
    # count number of occurances of each
    for i in range(len(arr)): # O(n)
        count[arr[i]] += 1
    # get running sum
    for i in range(len(count)): #O(k)
        if i > 0:
            count[i] += count[i - 1]
    # placement
    for i in range(len(arr)): # O(n)
        sorted_array[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    # copy sorted array to original array.
    # This step is only necessary if you want to modify the original array.
    for i in range(len(arr)): # O(n)
        arr[i] = sorted_array[i]

    # if you want to return a sorted copy of the origial array,
    # you can return sorted_array
    return arr

def insertion_sort(arr):
    last_sorted_index = 0
    while last_sorted_index < len(arr) - 1:
        if arr[last_sorted_index + 1] < arr[last_sorted_index]: # already sorted
            value = arr[last_sorted_index + 1]
            for i in range(0, last_sorted_index + 1):
                if value < arr[i]:
                    new_value = arr[i]
                    arr[i] = value
                    arr[last_sorted_index + 1] = new_value
                    value = new_value
        last_sorted_index += 1
    return arr