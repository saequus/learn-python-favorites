import timeit
import random

# Example of using timeit module
# In this particular example 2nd, 3rd and 4th columns compare time spend
# while building range, list and dictionary

for i in range(10000, 100001, 20000):
    list_obj = []
    t = timeit.Timer(
        'random.randrange(%d) in range_obj' % i,
        'from __main__ import random, range_obj')

    range_obj = list(range(i))  # build range
    range_time = t.timeit(number=1000)

    list_obj.append(j for j in range(i)) # build list
    list_time = t.timeit(number=1000)

    dictionary_obj = {j: None for j in range(i)}  # build dictionary
    dictionary_time = t.timeit(number=1000)
    print(
        "%d, %10.3f, %10.3f,  %10.3f" % (
            i, range_time, list_time, dictionary_time))
