"""
define functions inside other functions
it is useful for finish a project by each tasks
toShopping:
    * make shopping list
    * lock door
    * drive car to store
    * pick up items
    * check out
    * drive back home
    * put items in place
https://realpython.com/primer-on-python-decorators/
inner function will not defined till parent function is called.
"""
def parent():
    print("Printing from the parent() function")

    def second_child():
        print("Printing from the second_child() function")

    def first_child():
        print("Printing from the first_child() function")

    first_child()
    second_child()

def main():
    pass
    """
    >>> parent()
    Printing from the parent() function
    Printing from the second_child() function
    Printing from the first_child() function
    """
if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    parent()