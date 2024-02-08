def bubbleSort(arr):
    # the number of passes in bbsort = n -1
    for i in range(len(arr)-1):
        # inner loop to compare the consecutive items
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]: 
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

# optimized implementation that ensures swapping doesn't occur for an already sorted array

def bubbleSortOpt(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                swapped = True
        if not swapped:
            #print(swapped)
            break;

    

if __name__ == "__main__":
    arr = [1,9,8,4,3,0]
    bubbleSort(arr)
    print(arr)

    arr2 = [3,6,0,5]
    bubbleSortOpt(arr2)
    print(arr2)