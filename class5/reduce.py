from functools import reduce

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

l = [1,2,3,4,5,6,7]

def func(x, y):
    return x+y

a = reduce(func, l)
print(a)