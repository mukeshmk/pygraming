# Maximum product subset of an array
# Given an array a, we have to find maximum product possible
# with the subset of elements present in the array.
# The maximum product can be single element also.

def maximumProductSubset(arr, n):
    if n == 1:
        return arr[0]
    
    prod = 1

    count_neg = 0
    count_zero = 0
    max_neg = float('-inf')


    for i in range(n):
        # count zeros
        if arr[i] == 0:
            count_zero += 1
            continue

        if arr[i] < 0:
            count_neg += 1
            max_neg = max(max_neg, arr[i])
        
        prod *= arr[i]

    # if all nos are 0s return 0
    if count_zero == n:
        return 0
    
    # if there are odd no of neg nos
    # reutrn the product without the biggest neg no
    if count_neg % 2 == 1:
        return int(prod/max_neg)
    
    return prod

if __name__ == "__main__":
    a = [ -1, -1, -2, 4, 3 ]
    print(maximumProductSubset(a, len(a)))
