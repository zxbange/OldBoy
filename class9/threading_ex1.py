import threading
import time

# def run(n):
#     time.sleep(2)
#     print("task ",n)
#
# t1 = threading.Thread(target=run, args=("t1",))
# t2 = threading.Thread(target=run, args=("t2",))
#
# t1.start()
# t2.start()

class MyThread(threading.Thread):

    def __init__(self, n, sleep_time):
        super(MyThread, self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):
        print("running task ", self.n)
        time.sleep(self.sleep_time)
        print("task %s done" %self.n)


t1 = MyThread("t1",2)
t2 = MyThread("t2",4)

t1.start()
t2.start()

t1.join()  # wait()

print("main thread....")
