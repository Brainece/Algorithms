def insertionSort(arr):
    """implementation of insertion sort, which treats the first element as sorted, and using the 
    corresponding elements as keys, to either place before or after the first element
    """
    size = len(arr)
    for i in range(1,size):
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key

    return arr



if __name__ == "__main__":
    arr1 = [13, 23, 25, 24, 19, 21, 12, 20, 27, 22, 9, 7]
    arr2 = [26, 16, 14, 8, 19, 21, 5, 12, 28, 7, 9, 17]

    insertionSort(arr1)
    insertionSort(arr2)

    print(arr1)
    print(arr2)



        