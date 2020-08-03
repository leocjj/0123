#!/usr/bin/python3
"""
Convert an integer to a string
"""


def int_to_string(n, base):
    # Convert an integer to a string
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return int_to_string(n // base, base) + convert_string[n % base]

if __name__ == '__main__':
    print(int_to_string(1453, 16))
    print(int_to_string(10, 2))
