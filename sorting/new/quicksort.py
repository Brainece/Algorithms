"""Implementation of quicksort which utilizes partion method to subdivide the initial arr into subarrays
partition method is based on the concept of pivot where a pivot element ensures all elements to the left are
less than the pivot element and elements to the right are greater than the pivot element"""

def partition(arr, l,h):
    pivot = arr[l] # select the first element as the pivot
    i,j = l,h # initialize the increments with the first element and the second element

    while (i<j): # repeat as long as the i increment is less than the j decrement
        if(arr[i] < pivot):
            i = i + 1
        if(arr[j] > pivot):
            j = j - 1
        arr[i], arr[j] = arr[j], arr[i]
    
    if i > j:
        # swap the pivot element with the element at position j
        pivot, arr[j] = arr[j], pivot
    
    return j

def quickSort(arr,l,h):
    if l < h:
        j = partition(arr, l, h)
        quickSort(arr, l,j)
        quickSort(arr, j+1, h)



if __name__ == "__main__":
    arr1 = [13, 23, 25, 24, 19, 21, 12, 20, 27, 22, 9, 7]
    arr2 = [26, 16, 14, 8, 19, 21, 5, 12, 28, 7, 9, 17]

    quickSort(arr1,0,len(arr1)-1)
    #quickSort(arr2, 0,len(arr2)-1)

    print("array 1: ", arr1)
    #print("array 2: ", arr2)

    


