def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    output = 1
    while k > 0:
        output *= n
        n -= 1
        k -= 1
    return output


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    output = 0

    while y != 0:
        output += y % 10
        y = y // 10
    return output


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    count = 0
    while n != 0:
        if count == 2:
            return True
        if n % 10 == 8:
            count += 1
        else:
            count = 0
        n = n // 10
    return count == 2


def double_eights2(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"

    last = False
    while n != 0:
        curr = n % 10
        if curr == 8 and last:
            return True
        elif curr == 8:
            last = True
        else:
            last = False
        n = n // 10
    return False


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10,2)
    2
    4
    6
    8
    10
    >>> a
    5
    """
    count = 0

    i = 1
    while i <= n:
        if i % k == 0:
            print(i)
            count += 1
        i += 1
    return count
