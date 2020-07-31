"""
Understand my wrapper function
"""
def my_timer(original):
    import time

    def wrapper(*args, **kwargs):
        # start timer
        t1 = time.time()
        # call original function
        result = original(*args, **kwargs)
        # calculate execution time
        t2 = time.time() - t1
        # other than call the original function, you can do more staff befer and after
        print(f'08: {original.__name__} ran in {t2:.3f} seconds.')
        # return original function result
        return result
    # return wrapper function. since wrapper function has the same set arguments as original
    # we can call my_timer and pass original function
    return wrapper

# define a function which take 2 seconds
def display_info(name, age):
    import time
    time.sleep(2) # simulate long process function
    print(f"16: display_info()... run with arguments: ({name}, {age})")

# define another function take 3 seconds
def anotherLongRun(parm1, parm2):
    import time
    time.sleep(3)
    print(f"23: another long run process with arguments({parm1}, {parm2})")

if __name__ == '__main__':
    # pass function to my_timer, my_timer return a function f1
    f1 = my_timer(display_info)
    # call the function
    f1("John", 23)

    # pass another function to my_timer
    f1 = my_timer(anotherLongRun)
    # call the function
    f1("Long", "Run...")

