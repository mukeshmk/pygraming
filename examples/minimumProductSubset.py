# https://www.geeksforgeeks.org/minimum-product-subset-array/
#
# Given an array a, we have to find minimum product possible
# with the subset of elements present in the array.
# The minimum product can be single element also.
def minProductSubset(arr, n):
    if n == 1:
        return arr[0]
    
    max_neg = float('-inf')
    min_pos = float('inf')
    count_neg = 0
    count_zero = 0

    prod = 1

    for i in range(n):
        # count zeros
        if arr[i] == 0:
            count_zero += 1
            continue

        # find min pos
        if arr[i] > 0:
            min_pos = min(min_pos, arr[i])

        # count neg no and find max neg no
        if arr[i] < 0:
            max_neg = max(max_neg, arr[i])
            count_neg += 1

        # multiply all no
        prod *= arr[i]

    # return 0 if all nos are 0
    # or if no negative nos are there and at least one 0 is there
    if count_zero == n or (count_neg == 0 and count_zero > 0):
        return 0
    # if all nos are pos return min pos no
    if count_neg == 0:
        return min_pos
    # if there are even no of negative numbers
    # return the value of the product without the max neg no
    # this makes it the product of all non zero without the smallest neg no
    if count_neg % 2 == 0 and count_neg != 0:
        return int(prod/max_neg)
    
    return prod


if __name__ == "__main__":
    a = [ -1, -1, -2, 4, 3 ]
    print(minProductSubset(a, len(a)))
