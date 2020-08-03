#!/usr/bin/python3
"""
Convert from a given base to base 10
"""
from stack import Stack


def convert_base(decimal, base):
    # Convert from a given base to base 10
    digits = '0123456789ABCDEF'
    remainder = Stack()
    while decimal > 0:
        rem = decimal % base
        remainder.push(rem)
        decimal //= base
    binary = ''
    while not remainder.is_empty():
        binary += digits[remainder.pop()]
    return binary

if __name__ == '__main__':
    print(convert_base(42, 2))
    print(convert_base(42, 16))
