#encoding=utf-8

def cube(n):
    for i in range(3):
        n *= n
    return n

n = 3
print ( cube(n) )