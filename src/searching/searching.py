# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):                     
    if end >= start:                                                # we don't want start and endpoints to cross
        midpoint = (start + end) // 2                               # floor division
        if target == arr[midpoint]:                                 # checking if the target is equal the midpoint
            return midpoint
        elif target > arr[midpoint]:
            return binary_search(arr, target, (midpoint + 1), end)  # only the greater chunck of array will be checked for target
        elif target < arr[midpoint]:                                # could also be an else statement
            return binary_search(arr, target, start, (midpoint - 1))
    return -1   

[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s    # t      # m             # e
# s = start, t = target, m = midpoint, e = endpoint
# recursion allows you to write less lines of code

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass

