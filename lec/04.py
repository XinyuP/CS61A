from math import pi, sqrt


def prime_factors(n):
    """Print the prime factors of n in nondecreasing order.

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
        k = smallest_prime_factor(n)
        n = n // k
        print(k)


def smallest_prime_factor(n):
    """Return the smallest k > 1 that evenly divides n."""
    k = 2
    while n % k != 0:
        k += 1
    return k


def fib(n):
    """Compute the nth Fibonacci number, for n >= 1."""

    pred, curr = 0, 1
    k = 1

    # alternate implementation:
    # pred, curr = 1, 0
    # k = 0
    # this one could compute the 0th Fibonacci number correctly

    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr


"""Generalization."""


def area(r, shape_constant):
    assert r > 0, 'A length must be positive.'
    return r * r * shape_constant


def area_square(r):
    # assert r > 0, 'A length must be positive.'
    # return r * r
    return area(r, 1)


def area_circle(r):
    # return pi * r ** 2
    return area(r, pi)


def area_hexagon(r):
    # return r * r * 3 * sqrt(3) / 2
    return area(r, 3 * sqrt(3) / 2)


# def sum_naturals(n):
#     """Sum the first N natural numbers.
#     >>> sum_naturals(5)
#     15

#     """

#     total, k = 0, 1
#     while k <= n:
#         total, k = total + k, k + 1
#     return total


# def sum_cubes(n):
#     """Sum the first N cubes of natural numbers.

#     >>> sum_cubes(5)
#     225

#     """

#     total, k = 0, 1
#     while k <= n:
#         total, k = total + k**3, k + 1
#     return total


def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def summation(n, term):
    """Sum the first n terms of a sequence.

    >>> summation(5, cube)
    225
    """

    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def sum_naturals(n):
    """Sum the first N natural numbers.
    >>> sum_naturals(5)
    15

    """
    return summation(n, identity)


def sum_cubes(n):
    """Sum the first N cubes of natural numbers.

    >>> sum_cubes(5)
    225

    """
    return summation(n, cube)


def make_adder(n):
    """Return a function that take one argument K and return K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    >>> make_adder(12)(23)
    35

    >>> make_adder(2000)(23)
    2023

    """
    def adder(k):
        return k + n
    return adder
