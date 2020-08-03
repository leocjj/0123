#!/usr/bin/python3
"""
Check if opening and closing symbols are balanced
"""
from stack import Stack


def balanced_symbols(string):
    # Check if opening and closing symbols are balanced
    s = Stack()
    balanced = True
    i = 0
    while i < len(string) and balanced:
        symbol = string[i]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        i += 1
    return balanced and s.is_empty()


def matches(open, close):
    # Check if opening and closing symbols match
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

if __name__ == '__main__':
    print(balanced_symbols('{({([][])}())}'))
    print(balanced_symbols('[{()]'))
