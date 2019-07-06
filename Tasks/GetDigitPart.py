# Return part with digit(s) if the string starts with one.


def get_digit_part(string) -> int:
    """ Returns part with digit(s) if the string starts with one.
    :param string:
    :return int:
    """
    negative = False
    punctuation_set = {
        '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"',
        '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>',
        ';', '?', '#', '$', ')', '/'}
    stack = str()
    if string == '' or string.isspace():
        return 0
    s = string.split()[0]
    if s.startswith('-'):
        negative = True
        s = list(s)
        s.pop(0)
    elif s.startswith('+'):
        negative = False
        s = list(s)
        s.pop(0)
    for i in range(len(list(s))):
        element = str(s[i])
        if element.isdigit():
            stack += element
        elif element in punctuation_set or element.isalpha():
            if stack == '':
                return 0
            else:
                break
    if stack == '':
        return 0
    else:
        number = int(stack)
        if number > 2147483648:
            return -2147483648 if negative else 2147483647
        elif number == 2147483648:
            return -2147483648 if negative else 2147483647
        else:
            return number * -1 if negative else number


# Driver Code

print(get_digit_part(''), 0)
print(get_digit_part('04356'), 4356)
print(get_digit_part('2345af324masdl3e'), 2345)
print(get_digit_part('asf2345af324masdl3e'), 0)
