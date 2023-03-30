"""
short-circuiting 

when the operator reaches an operand that allows them to make a conclusion about the expression

>>> False or 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> True and 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>


ZeroDivisionError: division by zero
>>> True or 1/0
True
>>> False and 1/0
False

"""


"""
Error messages

"""
