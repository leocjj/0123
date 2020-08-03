#!/usr/bin/python3
"""
Convert a string from infix to postfix
"""
from stack import Stack


def infix_to_postfix(string):
    # Convert a string from infix to postfix
    prec = {}
    prec['**'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    ops = Stack()
    postfix = []
    tokens = string.split()

    for token in tokens:
        if token.isdigit() or token.isalpha():
            postfix.append(token)
        elif token == '(':
            ops.push(token)
        elif token == ')':
            top = ops.pop()
            while top != '(':
                postfix.append(top)
                top = ops.pop()
        else:
            while not ops.is_empty() and prec[ops.peek()] >= prec[token]:
                postfix.append(ops.pop())
            ops.push(token)

    while not ops.is_empty():
        postfix.append(ops.pop())
    return ' '.join(postfix)

if __name__ == '__main__':
    print(infix_to_postfix('A * B + C * D'))
    print(infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )'))
    print(infix_to_postfix('( A + B ) * ( C + D )'))
    print(infix_to_postfix('( A + B ) * C'))
    print(infix_to_postfix('A + B * C'))
    print(infix_to_postfix('5 * 3 ** ( 4 - 2 )'))
