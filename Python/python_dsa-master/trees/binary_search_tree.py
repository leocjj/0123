#!/usr/bin/python3
# Implement binary search tree


class TreeNode:
    # Implement tree node
    def __init__(self, key, value, left=None, right=None, parent=None):
        # Initialize tree node
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        # Check if a node has a left child
        return self.left

    def has_right_child(self):
        # Check if a node has a right child
        return self.right

    def is_left_child(self):
        # Check if a node is a left child
        return self.parent and self.parent.left == self

    def is_right_child(self):
        # Check if a node is a right child
        return self.parent and self.parent.right == self

    def is_root(self):
        # Check if a node is a root
        return not self.parent

    def is_leaf(self):
        # Check if a node is a leaf
        return not (self.left or self.right)

    def has_any_children(self):
        # Check if a node has any children
        return self.left or self.right

    def has_both_children(self):
        # Check if a node has two children
        return self.left and self.right

    def splice_out(self):
        # Remove successor helper method
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def find_successor(self):
        # Find successor node
        successor = None
        if self.has_right_child():
            successor = self.right.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor

    def find_min(self):
        # Find minimum key in a subtree
        current = self
        while current.has_left_child():
            current = current.left
        return current

    def replace_node_data(self, key, value, left, right):
        # Replace the data in a node
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self

    def __iter__(self):
        # Iterate through nodes
        if self:
            if self.has_left_child():
                for elem in self.left:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right:
                    yield elem


class BinarySearchTree:
    # Implement binary search tree
    def __init__(self):
        # Initialize binary search tree
        self.root = None
        self.size = 0

    def length(self):
        # Return length
        return self.size

    def __len__(self):
        # Return length
        return self.size

    def __iter__(self):
        # Iterate through binary search tree
        return self.root.__iter__()

    def put(self, key, value):
        # Insert a new node in the tree
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current):
        # Insert helper method
        if key < current.key:
            if current.has_left_child():
                self._put(key, value, current.left)
            else:
                current.left = TreeNode(key, value, parent=current)
        else:
            if current.has_right_child():
                self._put(key, value, current.right)
            else:
                current.right = TreeNode(key, value, parent=current)

    def __setitem__(self, key, value):
        # Insert new node using [] notation
        self.put(key, value)

    def get(self, key):
        # Get the given node
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, current):
        # Get helper method
        if not current:
            return None
        elif current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        else:
            return self._get(key, current.right)

    def __getitem__(self, key):
        # Get node using [] notation
        return self.get(key)

    def __contains__(self, key):
        # Allow use of 'in' operation
        return self._get(key, self.root)

    def delete(self, key):
        # Delete a node
        if self.size > 1:
            remove = self._get(key, self.root)
            if remove:
                self.remove(remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        # Delete a node
        self.delete(key)

    def remove(self, current):
        # Remove a node
        if current.is_leaf():  # node is leaf
            if current == current.parent.left:
                current.parent.left = None
            else:
                current.parent.right = None
        elif current.has_both_children():  # node has both children
            successor = current.find_successor()
            successor.splice_out()
            current.key = successor.key
            current.value = successor.value
        else:  # node has one child
            if current.has_left_child():
                if current.is_left_child():
                    current.left.parent = current.parent
                    current.parent.left = current.left
                elif current.is_right_child():
                    current.left.parent = current.parent
                    current.parent.right = current.left
                else:
                    current.replace_node_data(current.left.key,
                                              current.left.value,
                                              current.left.left,
                                              current.left.right)
            else:
                if current.is_left_child():
                    current.right.parent = current.parent
                    current.parent.left = current.right
                elif current.is_right_child():
                    current.right.parent = current.parent
                    current.parent.right = current.right
                else:
                    current.replace_node_data(current.right.key,
                                              current.right.value,
                                              current.right.left,
                                              current.right.right)

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree[3] = 'red'
    tree[4] = 'blue'
    tree[6] = 'yellow'
    tree[2] = 'at'

    print(tree[6])
    print(tree[2])
