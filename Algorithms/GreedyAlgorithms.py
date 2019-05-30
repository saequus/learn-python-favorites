
# Greedy Algorithms

# 1.Activity Selection Problem


def print_max_activities(s, f):
    n = len(f)
    i = 0
    print(i)
    for j in range(1, n):
        if s[j] >= f[i]:
            print(j)
            i = j


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]

print_max_activities(s, f)



