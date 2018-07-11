

class Dog:

    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s:wang wang wang" %self.name)


dog1 = Dog('zx')
dog1.bulk()

dog2 = Dog('abbott')
dog2.bulk()
