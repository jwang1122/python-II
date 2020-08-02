"""
However, to understand decorators, it is enough to think about functions 
as something that turns given arguments into a value.
"""
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet(greeter_func, name):
    return greeter_func(name)

if __name__ == '__main__':
    print(greet(say_hello, "David"))
    print(greet(be_awesome, "John"))
