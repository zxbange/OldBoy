# 只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性

class Dog(object):
    n = "aaa"

    def __init__(self, name):
        self.name = name

    @staticmethod  # 实际上跟类没有什么关系了,但是仍可以使用实例调用
    def eat(food):
        # self.  # 不能调用类的方法
        print("%s is eating %s" % (food, "ddd"))


    @classmethod  # 类方法，只能访问类变量，不是访问实例变量
    def talk(self):
        print("%s is talking %s" % (self.n, 'dd')) # 这里调self.name会报错




d = Dog("Alex")
# d.eat("包子")
d.eat("包子")
d.talk()