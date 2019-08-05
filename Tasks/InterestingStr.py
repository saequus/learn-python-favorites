# https://leetcode.com/discuss/interview-question/350312/google-onsite-interesting-string


from functools import lru_cache


def interesting_string(s):
    @lru_cache(maxsize=len(s))
    def dfs(i):
        if i == len(s):
            return True
        j = i
        while j < len(s) and s[j].isdigit():
            k = int(s[i:j + 1])
            if dfs(j + k + 1):
                return True
            j += 1
        return False
    return dfs(0)


s = "4g12y6hunter"
print(interesting_string(s), True)

s = "124gray6hunter"
print(interesting_string(s), True)

s = "31ba2a"
print(interesting_string(s), False)

s = "3abc4defg3abc4defg3abc"
print(interesting_string(s), True)
