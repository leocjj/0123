#!/usr/bin/python3
"""
Simple implementation of Stack using lists
"""


class Stack:
    # Simple implementation of Stack using lists
    def __init__(self):
        # Initialize an empty Stack
        self.items = []

    def is_empty(self):
        # Check if it's empty
        return self.items == []

    def push(self, item):
        # Append an item
        self.items.append(item)

    def pop(self):
        # Pop the last item
        return self.items.pop()

    def peek(self):
        # Return the value of the last item
        return self.items[len(self.items) - 1]

    def size(self):
        # Return the size
        return len(self.items)
