import rx
import rx.operators as ops

source = rx.from_iterable([1, 2, 'foo', 4])

disposable = source.pipe(
    ops.map(lambda i: i - 1),
    ops.filter(lambda i: i % 2 == 0),
).subscribe(
    on_next=lambda i: print("on_next: {}".format(i)),
    on_completed=lambda: print("on_completed"),
    on_error=lambda e: print("on_error: {}".format(e)),
)

disposable.dispose()
print("Done!")