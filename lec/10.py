# Ordering

def cascade(n):
    """Print a cascade of prefixes of n.

    >>> cascade(1234)
    1234
    123
    12
    1
    12
    123
    1234
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)


def cascade2(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)


def inverse_cascade(n):
    """Print an inverse cascade of prefixes of n.

    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


def grow(n): return f_then_g(grow, print, n//10)
def shrink(n): return f_then_g(print, shrink, n//10)


# def helper(i):
#     if n // (10**i):
#         print(n)
#     else:
#         print(i)
#         helper(n // (10**i))
#         print(i)
# helper(math.floor(math.log10(n)))


# Tree recursion
def fib(n):
    """Compute the nth Fibonacci number.

    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def count_partitions(n, m):
    """Count the partitions of n using parts up to size m.

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    42
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    return count_partitions(n-m, m) + count_partitions(n, m-1)
