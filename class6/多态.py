# 多态
# 一个接口多个实现

class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    @staticmethod
    def animal_talk(obj):
        obj.talk()

    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


# def animal_talk(obj):
#     obj.talk()


d = Dog("陈荣华")
# d.talk()
#
c = Cat("许两位")
# c.talk()

Animal.animal_talk(d)
