from collections import deque

queue1=deque(maxlen=3)
queue1.append(1)
queue1.append(2)
queue1.append(3)
queue1.clear()
#print(queue1)

import queue as q
queue2=q.Queue(maxsize=3)
#print(queue2.empty())
queue2.put(1)
queue2.put(2)
queue2.put(3)
#print(queue2.qsize())
#print(queue2.full())
#print(queue2.get())
#print(queue2.qsize())

from multiprocessing import Queue

custom=Queue(maxsize=3)
custom.put(1)
custom.put(2)
custom.put(3)
custom.get()
#print(custom)
