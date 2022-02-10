class Singleton(object):
    def __new__(cls, name):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self,name):
        self.name = name

s1 = Singleton('singleton1')
print(s1)
print(s1.name)

s2 = Singleton('singleton2')
print(s2)
print(s2.name)
