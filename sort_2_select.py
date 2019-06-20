#coding=utf-8
#拿到已排序的最大值，比较未排序部分的最小值的index，最后做交换
def sort(arr):
    for i in range( len(arr) ):
        minIndex = i
        for j in range(i,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[minIndex]
        arr[minIndex] = arr[i]
        arr[i] = temp
    return arr

arr = [5,1,4,2]
print 'start'
newArr = sort(arr)
print str( newArr ) 