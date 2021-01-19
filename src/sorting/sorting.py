# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)                    
    merged_arr = [0] * elements                         # created a merged array with all 0s the lenght of arrA and arrB

    a_index = 0                                         # pointers
    b_index = 0

    for i in range(len(merged_arr)):
        if a_index > len(arrA) - 1:                     # checking if the a index is not in array A
            merged_arr[i] = arrB[b_index]               # set the next spot in the merged array to what comes next in array B
            b_index += 1                                # move forward in array B by incrementing b_index
        elif b_index > len(arrB) - 1:                   # checking if the b index is not in array B
            merged_arr[i] = arrA[a_index]
            a_index += 1                                # move forward in array A by incrementing a_index
        else:                                           # if array A and array B and their index values have not gone past the length of their arrays
            if arrA[a_index] > arrB[b_index]:           # is item in array A > than item in array B?
                merged_arr[i] = arrB[b_index]           # setting current position in merged array to item in array B at b_index
                b_index += 1                            # move forward in array B by incrementing b_index
            else:
                merged_arr[i] = arrA[a_index]
                a_index += 1                            # move forward in array A by incrementing a_index

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    midpoint = len(arr) // 2                # lines 28 - 35 will continue running until we have single item arrays
    left = arr[:midpoint]                   # gets everything before the midpoint not including the midpoint
    right = arr[midpoint:]                  # gets everything after the midpoint including the midpoint

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    arr = merge(left, right)                # arrays are being merged together & sorted with the merge function we created above

    return arr                              # final sorted array is returned

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):               # does not occupy extra space
    start_two = mid + 1                                 # already have a start parameter

    if arr[mid] <= arr[start_two]:
        return
    while start <= mid and start_two <= end:            # start and mid are pointers for our first array, mid and end are pointers for second array
        if arr[start] <= arr[start_two]:                # is element 1 in the right spot?
            start += 1
        else:                                           
            value = arr[start_two]                      # store the lesser item in value - this will allow us to overwrite what the first item in the array is
            index = start_two                           # stor the index for the lesser item
            while index != start:                       # shift elements between element 1 and element 2 to the right by 1
                arr[index] = arr[index] - 1             # move every item in the array over by 1 to allow for the lesser value to be at the front of the array
                index -= 1
            arr[start] = value                          # moved lesser item to array at start
        start += 1                                      # increment pointers to continue searching / sorting through array
        mid += 1
        start_two += 1

def merge_sort_in_place(arr, l, r):
    if l < r:
        m = l + (r - 1) // 2
        merge_sort_in_place(arr, l, m)                  # lines 67 & 68 are sorting first and second half of array
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
