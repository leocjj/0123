#!/usr/bin/python3
"""
Check if a string is a palindrome
"""
from deque import Deque


def palindrome(string):
    # Check if a string is a palindrome
    deque = Deque()
    for ch in string:
        deque.add_rear(ch)
    equal = True
    while deque.size() > 1 and equal:
        first = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            equal = False
    return equal

if __name__ == '__main__':
    print(palindrome('lsdkjfskf'))
    print(palindrome('radar'))
    print(palindrome('amanaplanacanalpanama'))
