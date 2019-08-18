# Task 10 – Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching


def is_match(s: str, p: str) -> bool:

    if not p:
        return not s

    first_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return (is_match(s, p[2:]) or
                first_match and is_match(s[1:], p))
    else:
        return first_match and is_match(s[1:], p[1:])


print(is_match('aerrr', 'aer..'))
print(is_match('aaaayut', 'a*..t'))
