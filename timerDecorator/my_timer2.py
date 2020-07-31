"""
add decorator to any function
"""
def my_timer(original):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original(*args, **kwargs)
        t2 = time.time() - t1
        print(f'11: {original.__name__} ran in {t2:.3f} seconds.')
        return result
    return wrapper

# add @my_timer decorator to any function to measure the time spent on the function call
@my_timer
def display_info(name, age):
    import time
    time.sleep(2) # simulate long process function
    print(f"20: display_info()... run with arguments: ({name}, {age})")
    return age

# Call the function as usual, because we use the decorator @my_timer
x = display_info("John", 23)
print(x)