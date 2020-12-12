matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
l = [[row[i] for row in matrix] for i in range(4)]
print(l)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

print(list(zip(*matrix)))
"""
Unpacking Argument Lists
when the arguments are already in a list or tuple but need to be unpacked 
for a function call requiring separate positional arguments.
"""

# similar as
l1 = list(zip(matrix[0], matrix[1], matrix[2]))
print(l1)


l = list(range(3,10))
print(l)

# similar as
args=(3,10)
l = list(range(*args)) # unpacking argument list
print(l)