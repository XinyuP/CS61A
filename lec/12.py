odds = [3, 5, 7, 9, 11]
list(range(1, 3))
[odds[i] for i in range(1, 3)]

odds[1:3]

odds[:3]


"""
>>> sum([[1],[2]],[])
[1, 2]

>>> sum([[1],[2]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'list'

>>> max(range(5))
4
>>> max(0,1,2,3,4)
4
>>> max(range(10), key=lambda x: 7-(x-4)*(x-2))
3
>>> bool(-1)
True
>>> bool(0)
False
>>> bool('')
False
>>> bool([])
False

>>> all(range(5))
False

>>> all(1,2,3,'')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: all() takes exactly one argument (4 given)

>>> all([1,2,3,''])
False

>>> any(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable

>>> any([0])
False
>>> any((0,1,2))
True
>>> any((0,1,''))
True
>>> any((0,''))
False


>>> 'curry = lambda f: lambda x: lambda y: f(x,y)'
'curry = lambda f: lambda x: lambda y: f(x,y)'
>>> exec('curry = lambda f: lambda x: lambda y: f(x,y)')
>>> curry
<function <lambda> at 0x000001BC498E3380>
>>> from operator import add
>>> curry(add)(2)(4)
6


>>> 'here' in "where"
True
>>> 'os' in 'o s'
False
>>> 'os' in 'oss'
True

>>> 23 in [2,3,4]
False
>>> [2,3] in [2,3,4]
False





"""
# >>> """ hello
# ... This is Bliare
# ... Have a nice day :)
# ... """
# ' hello\nThis is Bliare\nHave a nice day :)\n'


# Slicing

odds = [3, 5, 7, 9, 11]
list(range(1, 3))
[odds[i] for i in range(1, 3)]
odds[1:3]
odds[1:]
odds[:3]
odds[:]

# Aggregation

sum(odds)
sum({3: 9, 5: 25})
max(range(10))
max(range(10), key=lambda x: 7 - (x-2)*(x-4))
all([x < 5 for x in range(5)])
def perfect_square(x): return x == round(x ** 0.5) ** 2


any([perfect_square(x) for x in range(50, 60)])  # Try ,65)

# Dicts


def dict_demos():
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['X']
    # numerals['X-ray']
    # numerals[10]
    len(numerals)
    list(numerals)
    numerals.values()
    list(numerals.values())
    sum(numerals.values())
    dict([[3, 9], [4, 16]])
    numerals.get('X', 0)
    numerals.get('X-ray', 0)
    {1: 2, 1: 3}
    {[1]: 2}
    {1: [2]}


"""
>>> numerals = {'I': 1, 'V': 5, 'X': 10}
>>> numerals['X']
10
>>> # numerals['X-ray']
>>> # numerals[10]
>>> len(numerals)
3

>>> list(numerals)
['I', 'V', 'X']

>>> numerals.values()
dict_values([1, 5, 10])

>>> list(numerals.values())
[1, 5, 10]

>>> sum(numerals.values())
16


>>> {}
{}
>>> {1:'items'}
{1: 'items'}
>>> {1:['one','two'], 2: 'three'}
{1: ['one', 'two'], 2: 'three'}
>>> d = {1:['one','two'], 2: 'three'}
>>> d[1]
['one', 'two']
>>> d[2]
'three'
>>> len(d)
2
>>> d
{1: ['one', 'two'], 2: 'three'}
>>> d.values()
dict_values([['one', 'two'], 'three'])
>>> d.items()
dict_items([(1, ['one', 'two']), (2, 'three')])
>>> d.keys()
dict_keys([1, 2])
>>> len(d[1])
2
>>> len(d[2])
5
>>> {1: 'one', 1: 'two'}
{1: 'two'}


>>> {[1]: 'one', 1: 'two'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'


>>> {(1): 'one', 1: 'two'}
{1: 'two'}
>>> {(1, 2): 'one', 1: 'two'}
{(1, 2): 'one', 1: 'two'}
>>> {{1, 2}: 'one', 1: 'two'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> {{}: 'one', 1: 'two'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
>>> {{1: 2}: 'one', 1: 'two'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'



>>> dict([[3, 9], [4, 16]])
{3: 9, 4: 16}
>>> numerals.get('X', 0)
10
>>> numerals.get('X-ray', 0)
0
>>> {1: 2, 1: 3}
{1: 3}
>>> {[1]: 2}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> {1: [2]}
{1: [2]}

"""


def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which 
    match(k, v) is a true value.

    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}
    # return {k: [v for v in values if match(k, v)] for k in keys}


"""
>>> values = range(30, 50)
>>> values
range(30, 50)
>>> {k : v for v in values for k in keys}
{7: 49, 9: 49, 11: 49}
>>> {k : [v for v in values] for k in keys}
{7: [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 9: [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 11: [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]}
>>> values = range(30, 35)
>>> {k : [v for v in values] for k in keys}
{7: [30, 31, 32, 33, 34], 9: [30, 31, 32, 33, 34], 11: [30, 31, 32, 33, 34]}
>>> {k : [name * 2 for name in values if name > 33] for k in keys}
{7: [68], 9: [68], 11: [68]}
>>> {k : [name * 2 for name in values if name > 32] for k in keys}
{7: [66, 68], 9: [66, 68], 11: [66, 68]}
>>> {k : v for v in values for k in keys}
{7: 34, 9: 34, 11: 34}
>>> {k : v*3 for v in values for k in keys}
{7: 102, 9: 102, 11: 102}
"""
