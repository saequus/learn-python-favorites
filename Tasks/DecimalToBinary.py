def decimalToBinary(x):
    if x > 1:
        decimalToBinary(x // 2)

    print(x % 2, end='')


if __name__ == '__main__':
    decimalToBinary(255)
