#!/usr/bin/python3
"""
Simple implementation of Queue using lists
"""


class Queue:
    # Simple implementation of Queue using lists
    def __init__(self):
        # Initialize an empty Queue
        self.items = []

    def is_empty(self):
        # Check if it's empty
        return self.items == []

    def enqueue(self, item):
        # Insert an item at the back of the line
        self.items.insert(0, item)

    def dequeue(self):
        # Remove the item at the front of the line
        return self.items.pop()

    def size(self):
        # Return the size
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.is_empty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
