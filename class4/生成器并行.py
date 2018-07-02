#  协程
import time

def consumer(name):
    print("%s准备吃包子啦" %(name))
    while True:
        baozi = yield "123"
        print("包子【%s】来了，被【%s】吃了" %(baozi, name))


# c = consumer("张鑫")  # 这里之生成一个生成器
# c.__next__()
# baozi = "韭菜馅"
# print(c.send(baozi))
# baozi2 = "萝卜馅"
# c.send(baozi2)

def producer(name):
    c1 = consumer("A")
    c2 = consumer("B")
    c1.__next__()
    c2.__next__()
    print("%s开始做包子啦" %name)
    for i in range(10):
        time.sleep(1)
        print("%s做了包子%s" %(name, i))
        c1.send(i)
        c2.send(i)


producer("Abbott")