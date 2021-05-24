from rx import of, operators as op
import random
from rx.subject import Subject
"""
different way to pipe functions: Hot Observables
"""

subject_test = Subject()
subject_test.subscribe(lambda x: print("From sub1 {0}".format(x)))
subject_test.subscribe(lambda x: print("From sub2 {0}".format(x)))
test1 = of(1, 2, 3, 4, 5)
sub1 = test1.pipe(op.map(lambda a: a + random.random()))
subscriber = sub1.subscribe(subject_test)