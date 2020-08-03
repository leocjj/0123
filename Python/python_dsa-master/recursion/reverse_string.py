#!/usr/bin/python3
"""
Reverse a string
"""


def reverse_string(s):
    # Reverse a string
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

if __name__ == '__main__':
    print(reverse_string('brent'))
