def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ == "__main__":
    print(bubbleSort([2, 5, 3, 9, 8, 7, 1]))
    print(bubbleSort([1, 2, 3, 4, 6]))
    print(bubbleSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(bubbleSort([2, 5, 3, 9, 1, 2]))
    print(bubbleSort([2, 5, 3, 9]))