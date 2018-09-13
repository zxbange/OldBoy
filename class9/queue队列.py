import queue

q = queue.Queue(maxsize=3)  # 先进先出
q1 = queue.LifoQueue()  # 后进先出
q2 = queue.PriorityQueue()  # 存储时可设置优先级

q.put("d1")
q.put("d2")
q.put("d3")
# q.put("d4", block=False, timeout=5)  #放多了就会卡住

print(q.qsize())

print(q.get())
print(q.get())
print(q.get())
# print(q.get()) 如果取空了，这里就会等待
# print(q.get(block=False))
# print(q.get_nowait())

q2.put((10, "alex"))  # 存储时设置了优先级
q2.put((100, "zx"))
q2.put((-1, "aaa"))
print(q2.get())
print(q2.get())
print(q2.get())