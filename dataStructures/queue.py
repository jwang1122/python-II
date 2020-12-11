from collections import deque
"""
Queue: First in First Out (FIFO)
"""
queue = deque(["Eric", "John", "Michael", "Elle"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)