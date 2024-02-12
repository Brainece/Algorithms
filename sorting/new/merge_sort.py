def merge(A,B):
    """function to merge two sorted arrays"""
    m,n  = len(A), len(B)
    i=j=k=0 
    result = []

    while(i<m and j<n):
        if(A[i] < B[j]):
            result.append(A[i])
            #result[k] = A[i]
            i +=1

        else:
            result.append(B[j])
            #result[k] = B[j]
            j +=1
        
        k+=1

    # copy the remaining items to the end of the list
    while (i<m):
        result.append(A[i])
        #result[k] = A[i]
        i +=1
        k += 1
    while (j<n):
        result.append(B[j])
        #result[k] = B[j]
        j +=1
        k +=1
        
    return result

def mergeSort(arr):
    size = len(arr)
    if size <=1:
        return arr
    else:
        mid = size // 2
        #L = arr[:mid]
        #R = arr[mid:]
        
        L = mergeSort(arr[:mid])
        R = mergeSort(arr[mid:])
        
        return merge(L,R)      


if __name__ == "__main__":
    arr1 = [13, 23, 25, 24, 19, 21, 12, 20, 27, 22, 9, 7]
    arr2 = [26, 16, 14, 8, 19, 21, 5, 12, 28, 7, 9, 17]

    mergeSort(arr1)
    mergeSort(arr2)

    print("array 1: ", mergearr1)
    print("array 2: ", arr2)
