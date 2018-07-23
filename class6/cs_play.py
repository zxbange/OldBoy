class Role:
    n = 123  #类变量, 节省开销
    name = "我是类name"
    n_list = []
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        # 构造函数 在实例化时，进行类的初始化的工作
        self.name = name  # 实例变量（静态属性），作用域是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value  # 私有属性
        self.money = money

    def shot(self):  # 类的方法，功能（动态属性）
        print("shooting...")

    def got_shot(self):
        self.__life_value -= 50  # 对属性做了修改
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name, gun_name))

    def show_status(self):
        print("name: %s weapen: %s life_value: %s" % (self.name, self.weapon, self.__life_value))

    def __shot(self):  # 私有方法
        print("aaa")

    def __del__(self):  # 析构函数/方法
        print("%s 彻底死了。。。。" %self.name)


r1 = Role('Alex', 'police', 'AK47') # 生成一个角色,实例化  Role类的实例
# Role(r1, 'Alex', 'police', 'AK47') 这里的r1就是self，所以构造函数必须由self
# r1.name = 'Alex'
# r1.role = 'police'
# r1.
r2 = Role('Jack', 'terrorist', 'B22')    #生成一个角色
#
# r1.buy_gun("AK47")  # 相当于Role.buy_gun(r1), r1同样还是self，所以类里每个函数都要由self
# print(r1.life_value)
#
#
# r1.name = "张鑫"
# r1.bullet_proof = True
#
#
# print(Role.n)
# print(r1.n, r1.name, r1.bullet_proof, r1.weapon)  # 先在实例本身找是否有对应name属性，如果没有，会去类中找
#
# del r1.weapon # 被删除
# print(r1.n, r1.name, r1.bullet_proof)  #
#
# r1.n = "改变类变量"  # 相当于给r1的n属性赋值，并没有改变类变量
# print(r2.n)
#
# r1.n_list.append("from r1")
# r2.n_list.append("from r2")
# print(r2.n_list)
# print(Role.n_list)
r1.got_shot()
r1.show_status()