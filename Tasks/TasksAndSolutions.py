# Задачи можно найти тут:
# https://informatics.mccme.ru/course/view.php?id=974


# Задача №1619. Смайлики
# https://informatics.mccme.ru/mod/statements/view3.php?id=17548&chapterid=1619


def count_smiles(s):
    result, i = 0, 0
    while i < len(s) - 1:
        if s[i] == ';' or s[i] == ':':
            i += 1
            while s[i] == '-' and i < len(s) - 1:
                i += 1
            if s[i] == '[' or s[i] == ']' or s[i] == '(' or s[i] == ')':
                result += 1
        else:
            i += 1
    return result


s = ':-)(dj:)djdns.()())))--(:-:]----:;-;-K[]--:-);;---'
print(count_smiles(s))


# Задача №1323. Префикс-функция
# https://informatics.mccme.ru/mod/statements/view3.php?id=17548&chapterid=1323
x = 'abracadabradomabraca'


def prefix_func(s):
    n = len(s)
    i, result = 1, [0]
    while i < n:
        left = 0
        right = i
        result.append(left)
        while right < n and s[left] == s[right]:
            left += 1
            right += 1
            result.append(left)
            i += 1

        i += 1
    return result


print(prefix_func(x))


