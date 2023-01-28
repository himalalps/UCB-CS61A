# Prime factorization
from operator import mul
from math import sqrt


def prime_factors(n):
    """Print the prime factors of positive integer n
       in non-decreasing order.

    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_factor(n)
        print(k)
        n = n // k


def smallest_factor(n):
    """Return the smallest factor of n greater than 1."""
    k = 2
    while n % k != 0:
        k = k + 1
    return k

# Control


def if_(c, t, f):
    if c:
        return t
    else:
        return f


def real_sqrt(x):
    if x >= 0:
        return sqrt(x)
    else:
        return 0

# Logical expressions


def has_big_sqrt(x):
    """Return whether x has a big square root.

    >>> has_big_sqrt(1000)
    True
    >>> has_big_sqrt(100)
    False
    >>> has_big_sqrt(0)
    False
    >>> has_big_sqrt(-1000)
    False
    """
    return x > 0 and sqrt(x) > 10

# Functions as arguments


def sum_naturals(n):
    """Sum the first N natural numbers.

    >>> sum_naturals(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total


def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def pi_term(k):
    return 8 / mul(k * 4 - 3, k * 4 - 1)


summation(1000000, pi_term)

# Local function definitions; returning functions


def make_adder(n):
    """Return a function that takes one argument K and returns K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder


make_adder(2000)(22)
