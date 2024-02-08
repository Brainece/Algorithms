"""def merge(A, B):
    i = j = k = 0
    m, n = len(A), len(B)
    result = []

    while i < m and j < n:
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
        while i < m:
            result.append(A[i])
            i += 1
        while j < m:
            result.append(B[j])
            j += 1

        return result"""
"""
def iterativeMergeSort(arr):
    #Implementation of 2-way merge sort, an iterative approach that uses the bottom up approach to solve the problem
    n = len(arr)
    size = 1
    sort_result = []

    if size <=1:
        return
    else:
        temp = []
        for i in range(0,size, 2):
            # loop through the elements 
            output = merge(arr[i], arr[i+1])
            temp.append(output)
    return temp
    

print(iterativeMergeSort([9,3,7,5,6,4,8,2]))"""
def merge(S, temp, From, mid, to):
     
    a = From
    b = From
    c = mid + 1
 
    while b <= mid and c <= to:
        if S[b] < S[c]:
            temp[a] = S[b]
            b = b + 1
        else:
            temp[a] = S[c]
            c = c + 1
        a = a + 1
 
    # remaining elements
    while b < len(S) and b <= mid:
        temp[a] = S[b]
        a = a + 1
        b = b + 1
 
    # copy back 
    for b in range(From, to + 1):
        S[b] = temp[b]
 
 
# Iterative sort
def Merge_Sort(S):
 
    low = 0
    high = len(S) - 1
 
    # sort list
    temp = S.copy()
 
    d = 1
    while d <= high - low:
 
        for b in range(low, high, 2*d):
            From = b
            mid = b + d - 1
            to = min(b + 2*d - 1, high)
            merge(S, temp, From, mid, to)
 
        d = 2*d
 
# Iterative implementation

S = [4, 2, 3, 1, 6, 5]
print("The Original array is: ", S)
Merge_Sort(S)
print("Array after sorting is: ", S)
"""if __name__ == '__main__':
 
    #driver code
    S = [4, 2, 3, 1, 6, 5]
    print("The Original array is: ", S)
    Merge_Sort(S)
    print("Array after sorting is: ", S)
"""
    

