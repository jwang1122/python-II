"""
Example of map with multiple iterables
"""
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l = list(map(lambda x, y: x+y, l1, l2))
print(l)

t1 = tuple(range(5))
t2 = (11,12,13,14,15)
t = tuple(map(lambda x, y: x*y, t1, t2))
print(t)
l = list(map(lambda x,y:x*y, t1, t2))
print(l)

l = list(filter(lambda x: x<42, l))
print(l)