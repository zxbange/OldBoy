# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# map()传入的第一个参数是func，即函数对象本身。由于结果a是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

def func(x):
    return x*x

l = [1,2,3,4,5,6,7]

a = map(func, l)

print(list(a))


