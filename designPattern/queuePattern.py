"""
Queue: First In First Out (FIFO)
put(): add one element into the Queue.
get(): remove one element from the Queue, and return the element.
qsize(): return current number of elements in the Queue.
empty(): return True if the Queue is empty, False otherwise
full(): Return True if there are maxsize items in the queue.
"""
from queue import Queue

q = Queue(5)

#put items at the end of the queue
for x in range(4):
   s = "item-" + str(x)
   print(f"put '{s}' into queue.")
   q.put(s)

#remove items from the head of the queue
print(q.qsize())
while not q.empty():
   print (q.get())
print(q.empty())
print(q.full())