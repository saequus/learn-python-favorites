# ============================================================================
# =========================== Make JOIN Realization ==========================
# ============================================================================

dict1 = {}
dict2 = {}

n1 = int(input())

for i in range(n1):
    data = [int(_) for _ in input().split()]
    if data[0] in dict1:
        dict1[data[0]].append(data[1])
    else:
        dict1.setdefault(data[0], data[1])

n2 = int(input())

for i in range(n2):
    data = [int(_) for _ in input().split()]
    if data[0] in dict2:
        dict2[data[0]].append(data[1])
    else:
        dict2.setdefault(data[0], data[1])

join_type = input()
result = []
max_key_number = max(max(dict1.keys()), max(dict2.keys()))

if join_type == 'FULL':
    for i in range(1, max_key_number + 1):
        if i in dict1.keys() and i in dict2.keys():
            result.append([i, dict1[i], dict2[i]])
        elif i in dict1.keys():
            result.append([i, dict1[i], 'NULL'])
        elif i in dict2.keys():
            result.append([i, 'NULL', dict2[i]])
        else:
            pass
elif join_type == 'LEFT':
    for i in range(1, max_key_number + 1):
        if i in dict1.keys() and i in dict2.keys():
            result.append([i, dict1[i], dict2[i]])
        elif i in dict1.keys():
            result.append([i, dict1[i], 'NULL'])
        else:
            pass
elif join_type == 'RIGHT':
    for i in range(1, max_key_number + 1):
        if i in dict1.keys() and i in dict2.keys():
            result.append([i, dict1[i], dict2[i]])
        elif i in dict2.keys():
            result.append([i, 'NULL', dict2[i]])
        else:
            pass
elif join_type == 'INNER':
    for i in range(1, max_key_number + 1):
        if i in dict1.keys() and i in dict2.keys():
            result.append([i, dict1[i], dict2[i]])
        else:
            pass
else:
    pass


print(len(result))
for j in result:
    for i in range(len(j)):
        if i != len(j) - 1:
            print(j[i], end=' ')
        else:
            print(j[i])


# Examples:

# Example 1
# (input this)
# 3
# 1 2
# 3 4
# 5 6
# 3
# 1 3
# 3 5
# 7 9
# INNER
# Result to example 1
# 2
# 1 2 3
# 3 4 5

# Example 2
# (input this)
# 3
# 1 2
# 3 4
# 5 6
# 3
# 1 3
# 3 5
# 7 9
# LEFT
# Result to example 2
# 3
# 1 2 3
# 3 4 5
# 5 6 NULL

# Example 3
# (input this)
# 3
# 1 2
# 3 4
# 5 6
# 3
# 1 3
# 3 5
# 7 9
# RIGHT
# Result to example 3
# 3
# 1 2 3
# 3 4 5
# 7 NULL 9

# Example 4
# (input this)
# 3
# 1 2
# 3 4
# 5 6
# 3
# 1 3
# 3 5
# 7 9
# FULL
# Result to example 4
# 4
# 1 2 3
# 3 4 5
# 5 6 NULL
# 7 NULL 9
