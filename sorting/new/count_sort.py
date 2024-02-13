
def countSort(arr):
    """Implementation of count sort uses the frequency of the occurences of the elements in 
    an array to return a sorted array"""

    n = len(arr) # store the count of elements
    key = max(arr) # max value used as the key

    # initialize a count_arr of key length with initial values as zero
    count_arr = [0] * (key+1)
    # initialize an output array of size n with intial zero values
    output = [0] *  n

    # determine the count of occurence of each item and store the occurence by incrementing in the count_arr
    for elem in arr:
        count_arr[elem] += 1
    
    #print(arr)
    
    # calculate the cummulative occurences and store in count_arr    
    for i in range(1,key+1):
        count_arr[i] = count_arr[i] + count_arr[i-1]
    
    #print(arr)
        
    # map the cummulative count to the output array

    for elem in reversed(arr):
        output[count_arr[elem] - 1] = elem
        count_arr[elem] -= 1

    # copy back to the original array
    for i in range(n):
        arr[i] = output[i]   

    return arr

if __name__ == "__main__":
    arr1 = [13, 23, 25, 24, 19, 21, 12, 20, 27, 22, 9, 7]
    arr2 = [26, 16, 14, 8, 19, 21, 5, 12, 28, 7, 9, 17]

    countSort(arr1)
    countSort(arr2)

    print("array 1: ", arr1)
    print("array 2: ", arr2)

    