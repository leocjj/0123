#!/usr/bin/python3
"""
Simple implementation of Deque using lists
"""


class Deque:
    # Simple implementation of Deque using lists
    def __init__(self):
        # Initialize an empty Deque
        self.items = []

    def is_empty(self):
        # Check if it's empty
        return self.items == []

    def add_front(self, item):
        # Insert an item at the front of the line
        self.items.append(item)

    def add_rear(self, item):
        # Insert an item at the back of the line
        self.items.insert(0, item)

    def remove_front(self):
        # Remove the item at the front of the line
        return self.items.pop()

    def remove_rear(self):
        # Remove the item at the back of the line
        return self.items.pop(0)

    def size(self):
        # Return the size
        return len(self.items)

if __name__ == '__main__':
    d = Deque()
    print(d.is_empty())
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())
