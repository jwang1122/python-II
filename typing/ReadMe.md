# Typing modules

* [Website](https://www.journaldev.com/34519/python-typing-module)
    - def <function name>(<argument>[:argument type]) [-> return type]:

## run code without issue, check fund error
```
pip install mypy
mypy level2/typing/typing1.py
```

output:

```
level2/typing/typing1.py:10: error: Argument 1 to "print_list" has incompatible type "int"; expected "List[int]"
Found 1 error in 1 file (checked 1 source file)
```

## use int for float has no issue
```
mypy level2/typing/circleTest.py
```

## use float for int cause error
- typing2.py > Vector = List[int]

## Find issue before going to production

```
mypy level2/typing/typing3.py
```

output:

```
level2/typing/typing3.py:19: error: Dict entry 1 has incompatible type "int": "str"; expected "str": "str"
Found 1 error in 1 file (checked 1 source file)
```