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
