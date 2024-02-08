def selectionSort(arr):
    """Implementation of selection sort in Python"""

    size = len(arr)
    for i in range(size):
        min_idx = i

        for j in range(i+1, size):
            if arr[j] <  arr[min_idx]:
                min_idx= j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    
    return arr

#print(selectionSort([14,33,27,10,35,19,42,44]))

arr2 = [26, 16, 14, 8, 19, 21, 5, 12, 28, 7, 9, 17]
print(selectionSort(arr2))

        