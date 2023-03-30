def apply_twice(f, x):
    return f(f(x))


########################
def square(x):
    return x * x


def triple(x):
    return 3 * x


def compose1(f, g):
    def h(x):
        return f(g(x))
    return h


def make_adder(n):
    def adder(k):
        return k + n
    return adder


"""
>>> triple(5)
15
>>> square(5)
25
>>> haha = compose1(square, triple)
>>> haha(5)
225
>>> haha = compose1(triple, square)
>>> haha(5)
75
>>> haha = compose1(square, make_adder(2))
>>> haha(3)
25
>>> compose1(square, make_adder(2))(3)
25
>>> compose1(square, make_adder(2))(4)
36
"""

# # formal parameters of a function have a local scope
# def f(x, y):
#     return g(x)


# def g(a):
#     return a + y  # error


# f(1, 2)
