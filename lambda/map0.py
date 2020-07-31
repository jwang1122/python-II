"""
map 2 list to one
"""
l1 = list(range(1,11))
l2 = list(range(11,21))
l = list(map(lambda x,y:x*x+2*y, l1, l2))
print(type(l))
print(l)