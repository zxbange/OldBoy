import threading
import time

lock = threading.Lock()

def run(n):
    lock.acquire()  # 获取用户态锁，cpu在子线程计算完成之后，才会进入下一个子线程,但是程序又变成了串行
    global num
    time.sleep(0.5)
    num += 1
    lock.release()  # 释放锁

num = 0

t_objs = []
for i in range(50):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    t.start()
    t_objs.append(t)


for t in t_objs:  # 将循环子线程列表，同时等待50个线程，直到所有执行完毕
    t.join()

print("--------------all threads has finished", threading.current_thread())
print("num: ",num)
# 因为多线程，生成的子线程独立运行，所以主线程继续运行
# gil_lock全局解释器锁
