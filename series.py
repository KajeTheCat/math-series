
def fib_sequence(n):
    """
    return n!
    e.g. 0, 1, 1, 2, 3, 5, 8, 13
    """


def fibonacci(n):
    if n < 0:
        print('fail')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print('fib', fibonacci(12))


def lucas_sequence(n):
    """
    return n!
    e.g. 2, 1, 3, 4, 7, 11, 18, 29
    """


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


# print('lucas', lucas(12))


def sum_sequence(n):
    """
    return n!
    fib or lucas
    """


# the start to the fibonacci sequence
# the start to lucas sequence


def sum_series(n, a, b):
    if a == 0 and b == 1:
        return fibonacci(n)
    elif a == 2 and b == 1:
        return lucas(n)


print('sum', sum_series(15, 2, 1))
