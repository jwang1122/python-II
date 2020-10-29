"""
Return a function from function
"""
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

if(__name__ == "__main__"):
    first = parent(1)
    second = parent(2)
    print(first)
    print(second)
    print(first())
    print(second())
