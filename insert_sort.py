#coding=utf-8
def sort(arr):
    current=0
    for i in range(len(arr)-1):
        current = arr[i+1]
        preIndex = i
        while preIndex >= 0 and current < arr[preIndex]:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr

arr = [5,1,4,2]
new_arr = sort(arr)
print str(new_arr)

