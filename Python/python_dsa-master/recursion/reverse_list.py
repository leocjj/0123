#!/usr/bin/python3
"""
Reverse a list
"""


def reverse_list(l):
    # Reverse a list
    if not l:
        return l
    else:
        return l[-1:] + reverse_list(l[:-1])

if __name__ == '__main__':
    print(reverse_list(['a', 2, 'c', 4, 'e']))
