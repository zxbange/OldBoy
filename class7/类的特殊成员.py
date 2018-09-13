

# class Dog(object):
#     '''gougou'''
#     # aaa
#
#     def eat(self):
#         print("dog eat")
#
# print(Dog.__doc__)  # 打印类的描述信息


class Foo(object):

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        print('__getitem__', key)
        return self.data.get(key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] = value

    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()

result = obj['k1']  # 自动触发执行 __getitem__
obj['k2'] = 'alex'  # 自动触发执行 __setitem__
print(obj.data)
print(obj["name"])
del obj['k1']