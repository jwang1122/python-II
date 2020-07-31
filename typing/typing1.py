"""
mypy typing1.py
"""
from typing import Any, List

def print_list(a:List[int]) ->None:
    print(a)

print_list([1,2,3])
print_list(1)

"""
typing1.py:10: error: Argument 1 to "print_list" has incompatible type "int"; expected "List[int]"
Found 1 error in 1 file (checked 1 source file)
"""