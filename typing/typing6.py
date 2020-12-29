# String slicing function that returns a string from start index to end index. 
def slice(string:str, start: int, end: int) -> str: 
    return string[start:end] 
  
x = slice([1, 2, 3, 4, 5], 2, 4) # pass an list instead of string

print(x) # return a list

x = slice("this is a test.", 5,7)
print(x)

"""
(env) C:\\Users\\12818\\workspace\\python-II>mypy typing/typing6.py
typing\\typing6.py:5: error: Argument 1 to "slice" has incompatible type "List[int]"; expected "str"
Found 1 error in 1 file (checked 1 source file)
"""
