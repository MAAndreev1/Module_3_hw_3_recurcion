def test(*params):
    for i in params:
        print(i)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


test(1, 's', True, [1, 2, 3])
print('----------')
print(factorial(7))