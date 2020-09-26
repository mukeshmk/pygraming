def insertionSort(array):
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                    array[j-1], array[j] = array[j], array[j-1]
    return array

if __name__ == "__main__":
    print(insertionSort([2, 5, 3, 9, 8, 7, 1]))
    print(insertionSort([1, 2, 3, 4, 6]))
    print(insertionSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(insertionSort([2, 5, 3, 9, 1, 2]))
    print(insertionSort([2, 5, 3, 9]))
