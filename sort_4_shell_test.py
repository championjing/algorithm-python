#ending=utf-8
def sort(arr):
    length = len(arr)
    gap = int( len(arr)/2 )
    while (gap > 0):
        for i in range(0,length-gap,gap):
            for j in (i,0,-gap):
                if( arr[j] > arr[j+gap]):
                    temp = arr[j]
                    arr[j] = arr[j+gap]
                    arr[j+gap] = temp
                else:
                    break
        gap = int( len(arr)/2 )
    return arr

test_arr = [4,6,3,9,1,2,7]
print str(test_arr)
print str( sort(test_arr) )