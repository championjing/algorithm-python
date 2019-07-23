#encoding=utf-8
def sort(arr):
    length = len(arr)
    temp = None
    gap = len(arr)//2
    while( gap > 0 ):
        for i in range(gap,length):
            temp = arr[i]
            preIndex = i - gap
            while ( preIndex >= 0 and arr[preIndex] > temp):
                tempIndex = preIndex+gap
                arr[tempIndex] = arr[preIndex]
                preIndex -= gap
            arr[preIndex + gap] = temp
        gap = gap//2
    return arr

arr = [8,9,1,7,2,3,5,4,6,0]

print(str(arr))
res = sort(arr)
print(str( res ))
