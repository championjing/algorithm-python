def mergeSort(arr):
    if( len(arr) < 2 ):
        return arr
    mid = len(arr)//2
    left = arr[0,mid]
    right = arr[mid,len(arr)]
    return merge(left,right)

def merge(left,right):
    res = left+right
    i,j = 0
    for index in range( len(res) ):
        if( i>= len(left) ):
            j += 1
            res[index] = left[j]
        elif (j>=len(right)):
            i += 1
            res[index] = left[i]
        elif (left[i] > right[j]) :
            j += 1
            res[index] = right[j]
        else:
            i += 1
            res[index] = left[i]
    return res

arr = [8,9,1,7,2,3,5,4,6,0]

print(str(arr))
res = mergeSort(arr)
print(str( res ))   