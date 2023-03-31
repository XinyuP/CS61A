def remove(n, digit):
    """
    >>> remove(231, 3)
    21
    >>> remove(123412341234, 4)
    123123123
    """

    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last * 10 ** digits
            digits += 1
    return kept

########################################


def remove2(n, digit):
    """
    >>> remove2(231, 3)
    21
    >>> remove2(123412341234, 4)
    123123123
    """

    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept/10 + last
            digits += 1
    return round(kept * 10 ** (digits-1))


########################################

def trace1(fn):
    """
    Returns a version of fn that first prints before it is called.
    fn -- a function of 1 argument

    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced


@trace1
def square(x):
    return x * x

# is the same as
# def square(x):
#     return x * x
# square = trace1(square)


@trace1
def sum_squares_up_to(n):
    """
    >>> sum_squares_up_to(5)
    55

    """
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total
