#!/usr/bin/python3
"""Compute factorial of a non-negative integer supplied on the command line.

Usage:
    ./factorial.py N

This script reads a single integer argument N and prints N! (the factorial of N).
The implementation uses an iterative approach to avoid recursion limits.
"""

import sys

def factorial(n):
    """Return n! (factorial of n).

    n must be a non-negative integer. The function uses an iterative loop
    to compute the factorial and returns the result as an integer.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

f = factorial(int(sys.argv[1]))
print(f)
