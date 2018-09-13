'''
An event is a simple synchronization object;

the event represents an internal flag, and threads
can wait for the flag to be set, or set or clear the flag themselves.

event = threading.Event()

# a client thread can wait for the flag to be set
event.wait()

# a server thread can set or reset it
event.set()
event.clear()
If the flag is set, the wait method doesn’t do anything.
标志位设定了，代表绿灯，直接通行
If the flag is cleared, wait will block until it becomes set again.
标志位被清空，代表红灯，wait等待变绿灯
Any number of threads may wait for the same event.
'''

import threading
import time

event = threading.Event()
def lighter():
    count = 0
    event.set()
    while True:
        if count > 5 and count < 10:  # 改成红灯
            event.clear()  # 清空标志位
            print("\033[41;1m红灯亮了\033[0m")
        elif count > 10:
            event.set()  # 设置标志位
            count = 0
        else:
            print("\033[42;1m绿灯亮了\033[0m")
        time.sleep(1)
        count += 1

a = 0
def car(name):
    while True:
        if event.is_set():
            print("[%s] is running..." % name)
            time.sleep(1)
        else:
            print("[%s] sees red light, waiting..." % name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" % name)

light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car, args=("Tesla",))
car1.start()