def BubbleSort(arr):
    """Implementation of the burble sort algorithnm in Python"""


    for i in range(len(arr) - 1):
        ## outer loop determines the number of passes, which == n -1
        for j in range(len(arr) - 1):
            # loop through the array and compare subsequent elements
            # minus 1 to prevent overflow
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def BubbleSortOpt(arr):
    """Implementation of the burble sort algorithnm in Python"""


    for i in range(len(arr) - 1):
        ## outer loop determines the number of passes, which == n -1
        swapped = False
        for j in range(len(arr) - 1):
            # loop through the array and compare subsequent elements
            # minus 1 to prevent overflow
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
            
            if not swapped:
                break
    return arr


        

#result = BubbleSort([21,6,9,33,3])
print(BubbleSortOpt([3,6,9,21,33]))
#print(result)
print()