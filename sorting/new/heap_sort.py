"""
Implementation of heap sort, which uses the heap creation and heap deletion to sort elements in a list
A heap is a complete binary tree with the parent element having a value greater than its descendants for the
case of a max-heap and less than all its descendants for the case of a min-heap
The heap creation can be done by inserting an element at a time  -upward insertion or through the heapify process
 which inserts elements downwards
"""

def heapify(arr, N, i):
    """the heap creation step"""
    largest = i # initialize largest as root
    left = 2*i + 1
    right = 2*i + 2

    #Check for left and right values and see if they are greater than the largest values 
    if left < N and arr[largest] < arr[left]:
        largest = left
    if right < N and arr[largest] < arr[right]:
        largest = right
    
    # if largest has been updated and is not equal to i then swap the values at both positions and heapify the arr again
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # heapify the arr
        heapify(arr,N, largest)

def heapSort(arr):
    N = len(arr)
     
    # build a max heap
    for i in range(N//2-1, -1, -1):
        heapify(arr,N,i)

    # one by one extract elements
    for i in range(N-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i] # swap
        heapify(arr,i,0)


if __name__ == "__main__":
    arr = [12,11,13,5,6,7]

    heapSort(arr)
    N = len(arr)

    print("Sorted array is")
    for i in range(N):
        print("%d" % arr[i], end=" ")







    

    

