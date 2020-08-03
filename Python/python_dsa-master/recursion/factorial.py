#!/usr/bin/python3
"""
Compute the factorial
"""


def factorial(n):
    # Compute the factorial
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    for i in range(21):
        print('The factorial of', i, 'is', factorial(i))
