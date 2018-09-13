import threading
import time

def run(n):
    print("task ",n)
    time.sleep(2)
    print("task done",threading.current_thread(),threading.active_count())

start_time = time.time()
t_objs = []
for i in range(5):
    t = threading.Thread(target=run, args=("t-%s" %i,))
    t.setDaemon(True) #  把当前线程设置为守护线程，一定要在start之前
    t.start()
    t_objs.append(t)


# for t in t_objs:  # 将循环子线程列表，同时等待50个线程，直到所有执行完毕
#     t.join()

print("--------------all threads has finished", threading.current_thread())
print("cost:", time.time()-start_time)

# 因为多线程，生成的子线程独立运行，所以主线程继续运行

