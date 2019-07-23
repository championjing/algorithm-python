#ending=utf-8
def sort(arr):
    for i in range(len(arr)-1):
        for j in range(i,-1,-1):
            if ( arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                break
    return arr

test_arr = [4,6,3,9,1,2,7,8]
print str(test_arr)
print str( sort(test_arr) )