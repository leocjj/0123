#!/usr/bin/python3
"""
Simulate the children's game hot potato
"""
from queue import Queue


def hot_potato(names, number):
    # Simulate the children's game hot potato
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    while queue.size() > 1:
        for i in range(number):
            queue.enqueue(queue.dequeue())
        print('Removing', queue.dequeue())
    return queue.dequeue()

if __name__ == '__main__':
    print('The winner is',
          hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))
