class Role:
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        # 构造函数 在实例化时，进行类的初始化的工作
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("%s just bought %s" %(self.name, gun_name))


r1 = Role('Alex', 'police', 'AK47') # 生成一个角色,实例化
# Role(r1, 'Alex', 'police', 'AK47') 这里的r1就是self，所以构造函数必须由self
# r1.name = 'Alex'
# r1.role = 'police'
# r1.
r2 = Role('Jack', 'terrorist', 'B22')    #生成一个角色

r1.buy_gun("AK47")  # 相当于Role.buy_gun(r1), r1同样还是self，所以类里每个函数都要由self
print(r1.life_value)

