#!/usr/bin/python3
"""
Simple implementation of OrderedList
"""
from node import Node


class OrderedList:
    # Simple implementation of OrderedList
    def __init__(self):
        # Initialize an OrderedList
        self.head = None

    def is_empty(self):
        # Check if the list is empty
        return self.head is None

    def add(self, item):
        # Add an item to the list
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() > item:
                break
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        # Return the length of the list
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        # Search for a node
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            elif current.get_data() > item:
                return False
            else:
                current = current.get_next()
        return False

    def remove(self, item):
        # Remove a node from the list
        current = self.head
        previous = None
        found = False
        while not found:
            if current is None or current.get_data() > item:
                print(str(item) + ' is not in the list')
                return
            elif current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head == current.get_next()
        else:
            previous.set_next(current.get_next())

    def index(self, item):
        # Return the position of the item in the list
        current = self.head
        pos = 0
        while current is not None:
            if current.get_data() == item:
                return pos
            elif current.get_data() > item:
                return None
            else:
                current = current.get_next()
                pos += 1
        return None

    def pop(self):
        # Remove and return the last item in the list
        current = self.head
        previous = None
        if self.size() == 0:
            return None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        if previous is None:
            self.head = None
        else:
            previous.set_next(None)
        return current.get_data()

    def __str__(self):
        # Print a linked list
        if self.head is None:
            return 'Empty list'
        current = self.head
        string = str(current.get_data())
        while current.get_next() is not None:
            current = current.get_next()
            string += ' -> ' + str(current.get_data())
        return string

if __name__ == '__main__':
    order = OrderedList()
    order.add(77)
    print(order)
    order.add(17)
    print(order)
    order.add(54)
    print(order)
    order.add(93)
    print(order)
    order.add(31)
    print(order)
    order.add(26)
    print(order)

    order.remove(77)
    print(order)
    order.remove(50)
    print(order)
    order.remove(100)
    print(order)

    print(order.index(31))
    print(order.index(50))
