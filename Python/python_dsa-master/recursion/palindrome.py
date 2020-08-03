#!/usr/bin/python3
"""
Check if a string is a palindrome
"""


def remove_white(s):
    # Remove characters that are not letters
    new = ''
    for ch in s:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            new += ch
    return new


def palindrome(s):
    # Check if a string is a palindrome
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    else:
        return palindrome(s[1:-1])

if __name__ == '__main__':
    print(palindrome(remove_white('lsdkjfskf')))
    print(palindrome(remove_white('radar')))
    print(palindrome(remove_white('a man, a plan, a canal, panama')))
    print(palindrome(remove_white('')))
    print(palindrome(remove_white("madam i'm adam")))
