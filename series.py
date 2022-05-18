
# Create two variables for the numbers to add during the sequence
# Create a counter to move through the sequence

def fibonacci(n):
    if n < 0:
        print('fail')
    elif n == 0:
        return 0
    elif n ==1 or n== 2:
        return 1
    else:
        return fibonacci(n-1)+(n-2)


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1)+lucas(n-2)


def sum_series(n, num_zero=0, num_one=1, ):