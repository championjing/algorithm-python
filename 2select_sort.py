def findSamllest(arr):
    smallest = arr[0] #存储最小值
    smallest_index = 0 # 存储最小值的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
# 对数组进行排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSamllest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr

print("******start*******")
my_list = [5,3,6,2,10]

print( selectionSort(my_list) ) 