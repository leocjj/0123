#!/usr/bin/python3
# Implement binary tree using lists of lists


def binary_tree(r):
    # Construct a list with a root node and two empty sublists
    return [r, [], []]


def insert_left(root, new_branch):
    # Add a left subtree
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    # Add a right subtree
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_value(root):
    # Return the value of the root
    return root[0]


def set_root_value(root, new_value):
    # Set the value of the root
    root[0] = new_value


def get_left_child(root):
    # Get the left child
    return root[1]


def get_right_child(root):
    # Get the right child
    return root[2]

if __name__ == '__main__':
    r = binary_tree(3)
    insert_left(r, 4)
    insert_left(r, 5)
    insert_right(r, 6)
    insert_right(r, 7)
    l = get_left_child(r)
    print(l)
    set_root_value(l, 9)
    print(r)
    insert_left(l, 11)
    print(r)
    print(get_right_child(get_right_child(r)))

    build = binary_tree('a')
    insert_left(build, 'b')
    insert_right(get_left_child(build), 'd')
    insert_right(build, 'c')
    insert_left(get_right_child(build), 'e')
    insert_right(get_right_child(build), 'f')
    print(build)
