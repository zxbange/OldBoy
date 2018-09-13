def bulk(self):
    print("%s is yelling..." %self.name)


class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" %(self.name, food))

    # def talk(self):
    #     print("%s is bulking..." %self.name)


d = Dog("Alex")
choice = input(">>:").strip()


print(hasattr(d, choice))
# print(getattr(d, choice))
# getattr(d, choice)()

if hasattr(d, choice):
    func = getattr(d, choice)
    func("aaa")
else:
    # setattr(d, choice, bulk)  # d.talk = bulk
    # d.talk(d)
    setattr(d, choice, 22)
    print(getattr(d, choice))

choice2 = input(">>:").strip()
delattr(d, choice2)
print(d.name)