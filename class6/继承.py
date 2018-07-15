# class People  经典类
class People(object):  # 新式类

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Relation(object):  # 此类用来做多继承
    def make_friends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))
        self.friends.append(obj)


class Man(People, Relation):
    def __init__(self, name, age, money):
        # People.__init__(self, name, age)  # 这里重写了父类的方法，所以需要先重写一遍
        super(Man, self).__init__(name, age)  # 作用同上, 但是如果多继承，上面方法就要写多遍
        self.money = money
        print("%s 出生就有%s" % (self.name, self.money))

    def piao(self):
        print("%s is piaoing.... 20s ... done" % self.name)

    def sleep(self):
        People.sleep(self)  # 调用父类方法
        print("man is sleeping...")  # 重构父类方法


class Woman(People, Relation):
    def get_birth(self):
        print("%s is born a baby..." % self.name)


m1 = Man("Alex", 22, 1000)
# m1.eat()
# m1.piao()
# m1.sleep()


w1 = Woman("ChengRonghua", 25)
# w1.get_birth()
# w1.name = "陈三炮"

m1.make_friends(w1)
print(m1.friends[0].name)