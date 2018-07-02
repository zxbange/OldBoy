# 生成器是一个对象，只能一个一个取，不能像列表一样,前
# 面的对象会被扔掉，无法向前取，只能像后取
# 之记录当前位置，只有一个__next__()方法，在2,7中是next()方法
a = (i*2 for i in range(1000000))  # 生成一个生成器

print(a)

# for i in a:
#     print(i)
# 0
# 2
# ...
# 334200
# ^CTraceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# KeyboardInterrupt
# 334204
# >>> a.__next__()
# 334206
# >>> a.__next__()
# 334208
# >>> a.__next__()
# 334210
# >>> a.__next__()
# 334212


# 斐波那契函数

def fib(max):  # yield 使其变为了一个生成器，不是函数
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # print(b)
        a, b = b, a+b
        n = n + 1
    return "done"

f = fib(10)
print(f)
print(f.__next__())
print("干点别的事")
print(f.__next__())
print(f.__next__())
print(f.__next__())

print("进入for循环")

# for i in f:
#     print(i)


while True:
    try:
        print(f.__next__())
    except StopIteration as e:
        print("Error:", e.value)
        exit()


