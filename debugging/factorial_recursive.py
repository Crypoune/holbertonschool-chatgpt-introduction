#!/usr/bin/python3
import sys

def factorial(n):
    """Calculates the factorial of a non-negative integer recursively.

    The factorial of a number n is the product of all positive integers less than or equal to n.
    By definition, the factorial of 0 is 1.

    Args:
        n (int): The non-negative integer for which to compute the factorial.

    Returns:
        int: The factorial of n.

    Raises:
        RecursionError: If n is too large (typically > 1000), Python's recursion limit may be exceeded.
        ValueError: If n is negative (factorial is not defined for negative numbers).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
