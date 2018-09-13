
# 只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性

class Dog(object):
    n = "aaa"

    def __init__(self, name):
        self.name = name
        self.__food = None

    @property  # 把一个方法变成一个静态属性
    def eat(self):
        print("%s is eating %s" % (self.name, self.__food))


    @eat.setter  # 给eat属性加属性
    def eat(self, food):
        print("set to food:", food)
        self.__food = food

    @eat.deleter  # 给eat删除属性
    def eat(self):
        del self.__food
        print("删完了")

    def __call__(self, *args, **kwargs):
        print("running call", args, kwargs)

    def __str__(self):
        return "<obj:%s>" %self.name


d = Dog("Alex")
d.eat # 这里就不能加括号调用
d.eat = "包子"
d.eat
#
# del d.eat
#
# d.eat

d(1,2,3,name="zx")  # 调用__call__方法
print(Dog.__dict__)  # 以字典方式打印类所有的属性和方法，不包括实例属性
print(d.__dict__)  # 以字典方式打印实例所有的属性和方法，不包括类属性

print(d)