from queue import Queue

q = Queue()
q.put("자료구조")
q.put("DB")
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())