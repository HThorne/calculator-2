"""Functions for common math operations."""

from functools import reduce

def add(list):
    """Return the sum of list of nums"""
    list.pop(0)
    nums =[]

    for item in list:
        nums.append(float(item))


    return reduce(lambda x, y: x + y, nums)


def subtract(num1, num2):
    """Return the value of num1 minus num2."""

    return num1 - num2


def multiply(list):
    """Multiply list items and return product of all."""
    list.pop(0)
    nums =[]

    for item in list:
        nums.append(float(item))

    return reduce(lambda x, y: x * y, nums)


def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""

    return num1 / num2


def square(num1):
    """Return the square of num1."""

    return num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2

def cube(num1):
    """Return the cube of num1"""

    return num1 ** 3