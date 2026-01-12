#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./factorial_recursive.py <non-negative-integer>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: argument must be an integer")
        sys.exit(1)

    if n < 0:
        print("Error: argument must be a non-negative integer")
        sys.exit(1)

    try:
        result = factorial(n)
    except RecursionError:
        print("Error: recursion limit exceeded for this input; try a smaller number or use an iterative implementation")
        sys.exit(1)

    print(result)