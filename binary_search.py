def binary_s(list, target):
    low = 0
    high = len(list) - 1
    loop = 0
    while low <= high:
        loop+=1
        print("run loop:"+str(loop))
        mid = (low + high)
        guess = list[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

print("******start*******")
my_list = [1,3,5,7,9]

print( binary_s(my_list, 3) ) 