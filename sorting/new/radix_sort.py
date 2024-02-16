def countSort(arr, exp):
    n = len(arr)
    #key = max(arr) + 1

    count_arr = [0] * 10 # initialize an empty array
    output = [0] * n

    for i in range(n):
       index = arr[i] // exp
       count_arr[index % 10 ] += 1

    for i in range(1, 10):
        count_arr[i] += count_arr[i-1]

    # build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count_arr[index % 10] -1 ] = arr[i]
        count_arr[index%10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

    return arr

def radixSort(arr):
    """
    Implementation of Radix Sort which utilizes lsb to msb, and count sort to sort an array
    """
    max_num = max(arr) # maximu number to determine number of bits
    exp = 1 # initialize the exp to ones

    while max_num // exp >= 1:
        countSort(arr,exp)
        exp *= 10 # increment by multiples of 10



if __name__ == "__main__":
    arr1 = [13, 23, 25, 24, 19, 21, 12, 20, 27, 22, 9, 7]
    arr2 = [26, 16, 14, 8, 19, 21, 5, 12, 28, 7, 9, 17]

    radixSort(arr1)
    radixSort(arr2)

    print("array 1: ", arr1)
    print("array 2: ", arr2)

    
