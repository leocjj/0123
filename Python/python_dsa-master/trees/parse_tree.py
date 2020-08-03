#!/usr/bin/python3
# Implement parse tree
from stack import Stack
from binary_tree import BinaryTree
import operator


def ParseTree(expr):
    # Implement parse tree
    my_list = expr.split()
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for i in my_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = stack.pop()
        else:
            try:
                current_tree.set_root_value(int(i))
                parent = stack.pop()
                current_tree = parent
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))
    return tree


def evaluate(tree):
    # Evaluate a parse tree
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul,
             '/': operator.truediv}
    left = tree.get_left_child()
    right = tree.get_right_child()
    if left and right:
        fn = opers[tree.get_root_value()]
        return fn(evaluate(left), evaluate(right))
    else:
        return tree.get_root_value()


def preorder(tree):
    # Preorder traversal
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree):
    # Postorder traversal
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_value())


def postorder_eval(tree):
    # Evaluate a parse tree using postorder traversal
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul,
             '/': operator.truediv}
    res1 = res2 = None
    if tree:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_value()](res1, res2)
        else:
            return tree.get_root_value()


def inorder(tree):
    # Inorder traversal
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_value())
        inorder(tree.get_right_child())


def print_expr(tree):
    # Print the expression
    string = ''
    if tree:
        string = '(' + print_expr(tree.get_left_child())
        string += str(tree.get_root_value())
        string += print_expr(tree.get_right_child()) + ')'
    return string

if __name__ == '__main__':
    tree = ParseTree('( ( 10 + 5 ) * 3 )')
    postorder(tree)
    print(print_expr(tree))
    print(postorder_eval(tree))
