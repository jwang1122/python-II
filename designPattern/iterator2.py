"""
Implementation of the iterator pattern with a generator

Traverses a container and accesses the container's elements.

python designPattern/iterator2.py -v 

Expected output:
5 items had no tests:
    __main__
    __main__.count_to
    __main__.count_to_five
    __main__.count_to_two
    __main__.main
0 tests in 5 items.
0 passed and 0 failed.
Test passed.
"""


def count_to(count):
    """Counts by word numbers, up to a maximum of five"""
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number
        # number # error out 


# Test the generator
count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)


def main():
    print(type(count_to_two))
    for s in count_to_two(): # count_to_two() function return an iterater
        print(s)
    """
    # Counting to two...
    >>> for number in count_to_two():
    ...     print(number)
    one
    two

    # Counting to five...
    >>> for number in count_to_five():
    ...     print(number)
    one
    two
    three
    four
    five
    """


if __name__ == "__main__":
    main()
    for s in count_to_five():
        print(s, end=' ')
    print()

    for s in count_to(8):
        print(s)

    import doctest

    doctest.testmod()
    # no output
    # python designPattern/iterator.py -v 
