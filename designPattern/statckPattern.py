"""
Stack: Last In First Out (LIFO)
put(): add one element to the stack
get(): remove one element from the stack, return the element
qsize(): return current number of elements in the Queue.
empty(): return True if the Queue is empty, False otherwise
full(): Return True if there are maxsize items in the queue.
"""
from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue(maxsize = 3)
 
# qsize() show the number of elements
# in the stack
print("initial stack size:",stack.qsize())
  
# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')
 
print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())