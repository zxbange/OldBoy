# 可以被next()调用并不断返回下一个值的对象成为迭代器： Iterator
# 生成器都是迭代器对象，但是list，dict，str虽然可以迭代，但不是迭代器
# 但是可通过iter()函数将list，dict等转变为迭代器

from collections import Iterable, Iterator

a = (i for i in range(10))

print(isinstance(a, Iterable))
print(isinstance(100, Iterable))
print(isinstance(a, Iterator))

print("===========列表b============")
b = [1, 2, 3, 4]
print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
b = iter(b)
print(isinstance(b, Iterator))

# range(10)在3中是迭代器，在2中xrange(10)是迭代器

# 在python2中
# >>> f = open("text.txt","r") 这里的f就是一个生成器
# >>> f.next()
# 'abc\n'
# >>> f.next()
# 'def\n'
# >>> f.next()
# 'hig\n'

# 在python3中

# >>> f = open("text.txt","r") 这里的f就是一个生成器
# >>> f.__next__()
# 'abc\n'
# >>> f.__next__()
# 'def\n'
# >>> f.__next__()
# 'hig\n'


# >>> f = open("text.txt","r")
# >>> a = f.readlines() 将生成器取各个元素变为列表
# >>> a
# ['abc\n', 'def\n', 'hig\n']
