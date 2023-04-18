def merge(A,B):
    """Function to merge two sorted arrays"""
    # A and B are arrays, and m and n are their sizes respectively
    m, n = len(A), len(B)
    #print(m, n)

    i = j = k = 0
    sorted_list = []

    while(i< m and j < n):
        if A[i] < B[j]:
            sorted_list.append(A[i])
            i += 1
        else:
            sorted_list.append(B[j])
            j += 1
        k += 1
    
    while i < m:
        sorted_list.append(A[i])
        i += 1
    while j < n:
        sorted_list.append(B[j])
        j += 1

    return sorted_list


def mergeSort(arr):
    size = len(arr)

    if size <= 1:
        return
    else:
        mid = size // 2
        L = arr[:mid]
        R = arr[mid:]
        
        mergeSort(L)
        mergeSort(R)
        return merge(L,R)
    


A = [14,33,27,10,35,19,42,44]
print(mergeSort(A))

#A = [1,5,9,15,17]
#B = [3,7,8,13,21,29,30]
#result = merge(A,B)
#print(result)
    
    
    
