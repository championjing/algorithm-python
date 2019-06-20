# coding=UTF-8
test_list = [ 1, 6, 3, 5, 3, 4 ,98,2,14,54,3,132,7] 
  
# print("查看 4 是否在列表中 ( 使用循环 ) : ") 
  
for n in test_list: 
    if(n == 4) : 
        print ("yes") 
  
# print("查看 4 是否在列表中 ( 使用 in 关键字 ) : ") 

if (4 in test_list): 
    print ("yes") 

def bubling(arr):
        for i in range(len(arr)):
                for j in range(len(arr)-i-1):
                        if( arr[j] > arr[j+1] ):
                                temp = arr[j]
                                arr[j] = arr[j+1]
                                arr[j+1] = temp
        return arr

print test_list
result = bubling(test_list)
print result
