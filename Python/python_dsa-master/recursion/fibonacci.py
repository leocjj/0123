#!/usr/bin/python3
"""
Print the Fibonacci sequence
"""


def fibonacci(n):
    # Print the Fibonacci sequence
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    for i in range(21):
        print(fibonacci(i))
