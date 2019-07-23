#!/usr/bin/python
#coding=utf-8
# 稳定排序，算法时间复杂度O(n^2)
arr = [1,3,4,2,8,0,3,6,14,9]
def sort(arr):
    current = None
    for i in range(len(arr)-1):
        current = arr[ i+1 ]
        preIndex = i
        while ( preIndex >= 0 and current < arr[preIndex] ):
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[ preIndex+1 ] = current
    return arr

print("over")
print( str(sort(arr)) )
