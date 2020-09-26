def selectionSort(array):
    # Traverse through all array elements
    for i in range(len(array)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        array[i], array[min_idx] = array[min_idx], array[i]

    return array

if __name__ == "__main__":
    print(selectionSort([2, 5, 3, 9, 8, 7, 1]))
    print(selectionSort([1, 2, 3, 4, 6]))
    print(selectionSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(selectionSort([2, 5, 3, 9, 1, 2]))
    print(selectionSort([2, 5, 3, 9]))
