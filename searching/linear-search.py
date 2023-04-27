def linearSearch(arr, key):
    """Finds an element in a list using linear search"""

    # loop through the array and find the key
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1

arr = [1,5,7,8,9,45]
result = linearSearch(arr,7)
if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)

