list1 = [1, 2, 3]
list2 = [4, 5, 6]

x = list2 + list1  # operator + related to __add__()
print("05:", x)  # output: 6 elements

print("07:", 8 in list1)  # __contains__ output: False
print("08:", len(list1))  # __len__ output: 7

print("11:", list1)  # __repr__

x = list1[1] >= 1  # __ge__
print("14:", x)  # output: True

s1 = "abc"
s2 = "john"
print("17:",s1>s2) # __gt__ implemented in str class

