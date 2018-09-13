import multiprocessing
import time

def run(name):
    time.sleep(2)
    print("hello", name)

if __name__ == "__main__":
    p = multiprocessing.Process(target=run, args=("aaa",))
    p.start()
    p.join()

from multiprocessing import Process
import os

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...\n' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.\n' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Process will start.\n')
#     p.start()
#     p.join()
#     print('Process end.\n')