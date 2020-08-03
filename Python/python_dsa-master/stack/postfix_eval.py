#!/usr/bin/python3
"""
Evaluate a postfix string
"""
from stack import Stack


def postfix_eval(string):
    # Evaluate a postfix string
    operands = Stack()
    tokens = string.split()
    for token in tokens:
        if token.isdigit():
            operands.push(int(token))
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            operands.push(do_math(token, op1, op2))
    return operands.pop()


def do_math(op, op1, op2):
    # Perform an operation
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

if __name__ == '__main__':
    print(postfix_eval('7 8 + 3 2 + /'))
