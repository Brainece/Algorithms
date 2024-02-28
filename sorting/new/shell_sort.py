def shellSort(arr):
    """Implementation of shell sort which uses reducing intervals between elements to sort the input array"""
    
    n = len(arr)
    interval = n//2

    while interval > 0:
        for i in range(interval,n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j-interval] > temp:
                arr[j] = arr[j-interval]
                j -= interval
            arr[j] = temp
        interval //=2

if __name__ == "__main__":
    arr1 = [13, 23, 25, 24, 19, 21, 12, 20, 27, 22, 9, 7]
    arr2 = [26, 16, 14, 8, 19, 21, 5, 12, 28, 7, 9, 17]

    shellSort(arr1)
    shellSort(arr2)

    print("array 1: ", arr1)
    print("array 2: ", arr2)



