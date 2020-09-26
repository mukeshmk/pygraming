def _binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return _binarySearch(arr, l, mid-1, x)
        else:
            return _binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def binarySearch(arr, element):
    return _binarySearch(arr, 0, len(arr), element)

if __name__ == "__main__":
    print(binarySearch([3, 2, 4, 1, 6, 5], 5))
