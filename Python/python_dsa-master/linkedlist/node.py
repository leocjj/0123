#!/usr/bin/python3
"""
Simple implementation of Node
"""


class Node:
    # Simple implementation of Node
    def __init__(self, data):
        # Initialize a Node
        self.data = data
        self.next = None

    def get_data(self):
        # Return the data
        return self.data

    def get_next(self):
        # Return the next node
        return self.next

    def set_data(self, data):
        # Set the data
        self.data = data

    def set_next(self, next):
        # Set the next node
        self.next = next

if __name__ == '__main__':
    temp = Node(93)
    print(temp.get_data())
