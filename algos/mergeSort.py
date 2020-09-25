def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1

        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1
    return arr

if __name__ == "__main__":
    print(mergeSort([2, 5, 3, 9, 8, 7, 1]))
    print(mergeSort([1, 2, 3, 4, 6]))
    print(mergeSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(mergeSort([2, 5, 3, 9, 1, 2]))
    print(mergeSort([2, 5, 3, 9]))
