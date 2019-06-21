def is_valid_parenthesis(s) -> bool:
    """ Check string of parenthesises whether all certain parentheses closes
    the block the open.
    :param s:
    :return bool:
    """
    opening_brackets = ['(', '[', '{']
    brackets_map = {')': '(', ']': '[', '}': '{'}
    if not s:
        return True

    if s[0] not in opening_brackets:
        return False

    stack = []
    for index, bracket in enumerate(s):
        if bracket in opening_brackets:
            stack.append(bracket)
        if bracket not in opening_brackets:
            try:
                last_opening_bracket = stack.pop()
                if last_opening_bracket != brackets_map[bracket]:
                    return False
            except IndexError:
                return False

    return not stack


not_valid = '({}))[](([))'
valid = '({})[](())'
print(is_valid_parenthesis(not_valid))
print(is_valid_parenthesis(valid))
