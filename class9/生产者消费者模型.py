import threading,time
import queue

q = queue.Queue(maxsize=10)

def Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("生产了骨头%s\n" % count)
        count += 1
        time.sleep(1)


def Consumer(name):
    while True:
    # while q.qsize() > 0:
        print("[%s] 取到 [%s]， 并且吃了它\n" %(name, q.get()))
        time.sleep(1)


p = threading.Thread(target=Producer, args=("Abbott",))
c = threading.Thread(target=Consumer, args=("ChengRonghua",))
c1 = threading.Thread(target=Consumer, args=("wangsen",))

p.start()
c.start()
c1.start()