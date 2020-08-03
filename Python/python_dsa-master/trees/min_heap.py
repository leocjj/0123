#!/usr/bin/python3
# Implement min heap


class MinHeap:
    # Implement min heap
    def __init__(self):
        # Initialize min heap
        self.list = [0]
        self.size = 0

    def percolate_up(self, i):
        # Percolate a new node up to its proper position
        while i // 2 > 0:
            if self.list[i] < self.list[i // 2]:
                self.list[i], self.list[i // 2] = (self.list[i // 2],
                                                   self.list[i])
            i //= 2

    def insert(self, new):
        # Insert a new node
        self.list.append(k)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_down(self, i):
        # Percolate the new root node down to its proper position
        while (i * 2) <= self.size:
            min_child = self.min_child(i)
            if self.list[i] > self.list[min_child]:
                self.list[i], self.list[min_child] = (self.list[min_child],
                                                      self.list[i])
            i = min_child

    def min_child(self, i):
        # Determine the minimum child of a node
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.list[i * 2] < self.list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete_min(self):
        # Delete the minimum node (always the root)
        min = self.list[1]
        self.list[1] = self.list[self.size]
        self.size -= 1
        self.list.pop()
        self.percolate_down(1)
        return min

    def build_heap(self, my_list):
        # Build a min heap
        i = len(my_list) // 2
        self.size = len(my_list)
        self.list = [0] + my_list
        while i > 0:
            self.percolate_down(i)
            i -= 1

if __name__ == '__main__':
    heap = MinHeap()
    heap.build_heap([9, 5, 6, 2, 3])
    print(heap.list[1:])
    print(heap.delete_min())
    print(heap.delete_min())
    print(heap.delete_min())
    print(heap.delete_min())
    print(heap.delete_min())
