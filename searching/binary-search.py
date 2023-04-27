def binarySearch(arr, key, l, h):
    """Implementation of binary search """
    
    while(l <= h):
        mid = (l + h) // 2

        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            h = mid -1 
        else:
            l = mid + 1
    
    return -1

arr = [1,5,7,8,9,45]
result = binarySearch(arr,30, 0, len(arr)-1)
if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)
