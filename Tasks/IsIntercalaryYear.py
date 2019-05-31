def isIntercalaryYear(n):
    if n % 4 != 0 or (n % 100 == 0 and n % 400 != 0):
        return '{} '.format(n) + 'year is usual.'
    else:
        return '{} '.format(n) + 'year is intercalary.'


print(isIntercalaryYear(1900))
