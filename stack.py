import queue

q1 = queue.Queue(10)  # FIFO The max size is 10.
for x in range(15):
    item = (x, x*x) # tuple
    q1.put(item)

    if (q1.full()): # if q full pop oldest one
        x = q1.get()

for x in range(q1.qsize()):
    item = q1.get()
    print(item)
