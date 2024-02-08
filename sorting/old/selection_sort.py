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

print(selectionSort([14,33,27,10,35,19,42,44]))


        