"""
Python Function Decorators
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html

Decorators allow you to inject or modify code in functions or classes. 
"""

def entryExit(original):
    def wrapper():
        print("entryExit() before original function call...")
        original()
        print("entryExit() after original function call...\n")
    return wrapper

@entryExit
def func1():
    print("inside func1...")

@entryExit
def func2():
    print("inside func2...")

func1()
func2()
