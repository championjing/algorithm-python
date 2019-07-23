#encoding=utf-8

def cube(n):
    return n**3

n = 3

def factorial(n):
    if n == 1: 
        return 1
    elif n==0:
        return 0
    elif n<0:
        raise RuntimeError("输入不能小于0")
    else:
        return factorial(n-1)*n

def count_pattern(strs,dict):
    if len(strs)==0:
        raise RuntimeError("匹配字符不能为空")
    res = 0
    for i in range(len(dict)):
        if dict[i] == strs[0]:
            skip = 1
            flag = False
            for si in range(1, len(strs) ):

                if i+skip <len(dict) and strs[si] == dict[i+skip]:
                    flag = True
                    skip += 1
                else:
                    flag = False
                    break
            if flag:
                res += 1
    return res

# print ( cube(n) )
# print( factorial(-1) )
str = ('a','b')
dict = ('a','b','c','e','b','a','b','f')
res = count_pattern( str, dict )
print( res )
str = ('a','b','a')
dict = ( 'g','a','b','a','b','a','b','a' )
res = count_pattern( str, dict )
print( res )