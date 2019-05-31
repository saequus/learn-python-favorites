import timeit
import random

for i in range(10000, 100001, 20000):
    g = []
    t = timeit.Timer('random.randrange(%d) in x' %i, 'from __main__ import random, x')
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    g.append(j for j in range(i))
    sec_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f,  %10.3f" % (i, lst_time, sec_time, d_time))




# for i in range(10000, 200001, 20000):
#     t = timeit.Timer('random.randrange(%d) in x'%i, 'from __main__ import random, x')
#     x = list(range(i))
#     lst_time = t.timeit(number=10000)
#     x = list(range(i))
#     lst_time2 = t.timeit(number=1000)
#     print("%d, %10.3f, %10.3f" % (i, lst_time, lst_time2))
#
#
# for i in range(10000, 100000, 10000):
#     t = timeit.Timer('random.randrange(%d) in x'%i, 'from __main__ import random, x')
#     x = list(range(i))
#     lst_time = t.timeit(number=10000)
#     x = {j: None for j in range(i)}
#     d_time = t.timeit(number=10000)
#     print("%d, %10f, %10f" % (i, lst_time, d_time))
