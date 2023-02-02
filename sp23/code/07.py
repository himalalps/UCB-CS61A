# Curry

from operator import add


def curry(f):
    return lambda x: lambda y: f(x, y)


make_adder = curry(add)
add_three = make_adder(3)

# Return


def end(n, d):
    """Print the final digits of N in reverse order until D is found.    

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None


def search(f):
    """Return the smallest non-negative integer x for which f(x) is a true value."""
    x = 0
    while True:
        if f(x):
            return x
        x += 1


def square(x):
    return x * x


def triple(x):
    return 3 * x


def inverse(f):
    """Return a function g(y) that returns x such that f(x) == y.

    >>> sqrt = inverse(square)
    >>> sqrt(16)
    4
    >>> inverse(triple)(15)
    5
    """
    return lambda y: search(lambda x: f(x) == y)

# Errors & Tracebacks


def f(x):
    return g(x - 1)


def g(y):
    return abs(h(y) - h(1 / y))  # remove paren


def h(z):
    return z * z  # remove return


print(f(12))  # remove 2
