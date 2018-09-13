'''
好吧，把一个方法变成静态属性有什么卵用呢？既然想要静态变量，那直接定义成一个静态变量不就得了么？well, 以后你会需到很多场景是不能简单通过 定义 静态属性来实现的， 比如 ，你想知道一个航班当前的状态，是到达了、延迟了、取消了、还是已经飞走了， 想知道这种状态你必须经历以下几步:

1. 连接航空公司API查询

2. 对查询结果进行解析

3. 返回结果给你的用户

因此这个status属性的值是一系列动作后才得到的结果，所以你每次调用时，其实它都要经过一系列的动作才返回你结果，但这些动作过程不需要用户关心， 用户只需要调用这个属性就可以，明白 了么？
'''
class Flight(object):
    def __init__(self,name):
        self.flight_name = name


    def checking_status(self):
        print("checking flight %s status " % self.flight_name)
        return  1

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0 :
            print("flight got canceled...")
        elif status == 1 :
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter
    def flight_status(self, status):
        print("set status to ", status)

f = Flight("CA980")
f.flight_status
f.flight_status = 2