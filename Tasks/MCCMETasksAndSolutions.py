# Tasks can be found here:
# https://informatics.mccme.ru/course/view.php?id=974


# Task №1619. Smiles
# https://informatics.mccme.ru/mod/statements/view3.php?id=17548&chapterid=1619


def count_smiles(s: str) -> int:
    """ Counts smiles in a string.
    Smiles are: ':' with any number of '-' and any number of '[' or ']'
    or '(' or ')' after it.
    :param s: str with text and smiles
    :return: int number of smiles
    """
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


find_smile = ':-)(dj:)djdns.()())))--(:-:]----:;-;-K[]--:-);;---'
print(count_smiles(find_smile))


# Task №1323. Prefix function
# https://informatics.mccme.ru/mod/statements/view3.php?id=17548&chapterid=1323
x = 'abracadabradomabraca'


def prefix_func(s: str) -> list:
    """
    Finds prefixes in the str that corresponds to the beginning of the str.
    Any number in the resulting list is number of corresponding letter in the
    current prefix to the beginning of the str.s
    :param s: str
    :return: list
    """
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


