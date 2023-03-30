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

##########################################
"""
Lambda 

>>> triple = lambda x: x ** 3
>>> square = lambda x: x**2
>>> triple(10)
1000
>>> square(2)
4
>>> square(10)
100

>>> (lambda x: x * x)(2)
4
>>> (lambda x: x * x)(5)
25
>>> (lambda x: x ** 3)(5)
125


>>> def sq(x):
...     return x**2
...
>>> sq
<function sq at 0x0000027122EA3380>

* only def gives the function an intrinsic name

>>> square
<function <lambda> at 0x0000027122EA32E0>

>>> (lambda x: x * x)
<function <lambda> at 0x0000027122EA34C0>

"""
