from series import fibonacci
from series import lucas
from series import sum_series


def test_fibonacci_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_fibonacci_four():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_fibonacci_five():
    actual = fibonacci(12)
    expected = 144
    assert actual == expected


def test_lucas_one():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_two():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_three():
    actual = lucas(8)
    expected = 47
    assert actual == expected


def test_lucas_four():
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_lucas_five():
    actual = lucas(12)
    expected = 322
    assert actual == expected


def test_sum_series_fib_one():
    assert sum_series(0, 0, 1) == 0


def test_sum_series_fib_two():
    assert sum_series(5, 0, 1) == 5


def test_sum_series_lucas_one():
    assert sum_series(3, 2, 1) == 4


def test_sum_series_lucas_two():
    assert sum_series(15, 2, 1) == 1364
