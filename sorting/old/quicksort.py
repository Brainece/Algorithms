#def Quicksort(arr):
#    """implementation of quick sort in python"""


def Partition(arr,l,h):
    """Determination of partition position"""   
    
    pivot = arr[l]
    i, j = l, h #pointer variables
    while i < j:
        if arr[i] < pivot:
            i += 1
        if arr[j] > pivot:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]

    if i > j:
        pivot, arr[j] = arr[j], pivot 
    
    return j

def quickSort(arr, l, h):
    """Implementation of quicks sort"""
    #l, h = 0, A.index[-1]
    if l < h:
        j = Partition(arr,l,h)
        quickSort(arr, l, j)
        quickSort(arr, j+1, h)



arr = [10,16,8,12,15,6,3,9,5]
arr2 = [8,7,6,1,0,9,2]
arr3 = [3,7,9,11]
arr4 = [11,9,29,7,2,15,28]
arr5 = [25,22,21,10]
#print(Partition(arr, 0, 8))
#quickSort(arr, 0,8)
quickSort(arr4,0,len(arr4)-1)
print(arr4)









