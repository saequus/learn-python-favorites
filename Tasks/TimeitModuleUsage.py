# import timeit
# import random
#
# for i in range(10000, 120001, 20000):
#     t = timeit.Timer('random.randrange(%d) in x' %i, 'from __main__ import random, x')
#     x = list(range(i))
#     list_time = t.timeit(number=1000)
#     x = [j for j in range(i)]
#     gen_time = t.timeit(number=1000)
#     x = {k: None for k in range(i)}
#     dict_time = t.timeit(number=1000)
#     print("%d, %10f, %10f, %10f" % (i, list_time, gen_time, dict_time))
#

# import timeit
# import random
#
# for i in range(10000, 100001, 20000):
#     g = []
#     t = timeit.Timer('random.randrange(%d) in x' %i, 'from __main__ import random, x')
#     x = list(range(i))
#     lst_time = t.timeit(number=1000)
#     g.append(j for j in range(i))
#     sec_time = t.timeit(number=1000)
#     x = {j: None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     print("%d, %10.3f, %10.3f,  %10.3f" % (i, lst_time, sec_time, d_time))
#


def one(x):
    return x * x


def two(y):
    return y + y

import timeit
import random

#
# for i in range(1000, 100000, 10000):
#     t = timeit.Timer('random.randrange(%d) in x' %i, 'from __main__ import random, x')
#     x = [one(i) for i in range(i)]
#     one_time = t.timeit(number=1000)
#     x = [two(i) for i in range(i)]
#     two_time = t.timeit(number=1000)
#     print("%d, %10f, %10f" % (i, one_time, two_time))


xrr = 'asdfj jf s  a g asdgj asdk e a d g asd. v ds w  dpsa d and d a.  e df l a pslnd add s a  d f  f f a\
    asdfj jf s  a g asdgj asdk e a d g asd v ds w  dpsa d and d a  e df. l a pslnd add s ad  asd sdf  f sdfkjlasdkflf a'


def spl(e):
    return e.split()


def cnt(e):
    return e.count(' ')


for i in range(10000, 180000, 30000):
    t = timeit.Timer('random.randrange(%d) in x' %i, 'from __main__ import random, x')
    x = [spl(xrr) for i in range(i)]
    one_time = t.timeit(number=1000)
    x = [cnt(xrr) for i in range(i)]
    two_time = t.timeit(number=1000)
    print("%d, %10f, %10f" % (i, one_time, two_time))
