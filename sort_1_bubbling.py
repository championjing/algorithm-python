#!/usr/bin/python
#coding=utf-8
# 稳定排序，算法时间复杂度O(n^2)
arr = [5,1,4,2]
for i in range(len( arr )):
    move = arr[i]
    print( str( move ) )

    for j in range( len(arr)-i-1 ):
        if arr[j]>arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
print("over")
print( str(arr) )
