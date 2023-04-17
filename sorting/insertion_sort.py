def insertionSort(arr):
    """Implementation of insertion sort in python"""

    # take the first element as already sorted
    size = len(arr)
    if size == 1:
        return arr
    else:
        for i in range(1, size):
            key = arr[i]
            j = i - 1

            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j = j - 1

            arr[j+1] = key
    
    return arr


print(insertionSort([9,5,1,4,3]))
