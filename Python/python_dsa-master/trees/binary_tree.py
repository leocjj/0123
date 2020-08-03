#!/usr/bin/python3
# Implement binary tree


class BinaryTree:
    # Implement binary tree
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        # Add a left subtree
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        # Add a right subtree
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right = self.right
            self.right = t

    def get_root_value(self):
        # Return the value of the root
        return self.key

    def set_root_value(self, obj):
        # Set the value of the root
        self.key = obj

    def get_left_child(self):
        # Get the left child
        return self.left

    def get_right_child(self):
        # Get the right child
        return self.right

if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.get_root_value())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_value())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root_value())
    r.get_right_child().set_root_value('hello')
    print(r.get_right_child().get_root_value())

    build = BinaryTree('a')
    build.insert_left('b')
    build.insert_right('c')
    build.get_left_child().insert_right('d')
    build.get_right_child().insert_left('e')
    build.get_right_child().insert_right('f')
    print(build)
