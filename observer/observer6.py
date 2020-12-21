import rx
"""
rx.create function example
"""
def f(observer, scheduler):
    observer.on_next(1)
    observer.on_next(2)
    observer.on_next(3)
    observer.on_completed()

x = rx.create(f)

x.subscribe(print)

test = rx.empty()
test.subscribe(
   lambda x: print("The value is {0}".format(x)),
   on_error = lambda e: print("Error : {0}".format(e)),
   on_completed = lambda: print("Job Done!")
)