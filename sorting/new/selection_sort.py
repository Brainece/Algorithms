
def selectionSort(arr):
    """implementation of selection sort which divides the array into sorted and unsorted portions,
    the leftmost portion being the sorted part and the other being the unsorted part.
    """
    size = len(arr) # store the size of the array
    for i in range(size):
        min_index = i # set the first element of the arr as the minimum element
        
        for j in range(i+1, size):
            # loop through the array to get the location of the minimum element
            if arr[j] < arr[min_index]:
                min_index = j
            

        if i != min_index: 
            # if returned min element is not equal to the assumed min then swap the elements\
            arr[i], arr[min_index] = arr[min_index], arr[i]
                
        
    return arr

if __name__ == "__main__":
    arr1 = [13, 23, 25, 24, 19, 21, 12, 20, 27, 22, 9, 7]
    arr2 = [26, 16, 14, 8, 19, 21, 5, 12, 28, 7, 9, 17]

    selectionSort(arr1)
    selectionSort(arr2)

    print("array 1: ", arr1)
    print(arr2)


