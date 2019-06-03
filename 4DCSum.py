def facto(arr):
    print("-----------")
    length = len(arr)
    if( length == 0):
        return 0
    elif (length == 1):
        return arr[0]
    else:
        mid = length//2
        print("mid:"+str(mid))
        low = arr[0:mid]
        print(low)
        high = arr[mid:length]
        print(high)
        return facto(low)+facto(high)

print("******start*******")
my_list = [1,3,5,7,9]

print( facto(my_list) ) 