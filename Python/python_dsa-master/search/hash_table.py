#!/usr/bin/python3
# Implement hash table


class HashTable:
    # Define HashTable
    def __init__(self):
        # Initialize HashTable
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        # Add a new key-value pair to the map
        # If the key is already there, replace old value with new value
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while (self.slots[next_slot] is not None and
                       self.slots[next_slot] != key):
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def hash_function(self, key, size):
        # Use simple % hash
        return key % size

    def rehash(self, old_hash, size):
        # Find the next available slot
        return (old_hash + 1) % size

    def get(self, key):
        # Given a key, return the value stored in the map or None
        start = self.hash_function(key, len(self.slots))
        pos = start
        while self.slots[pos] is not None:
            if self.slots[pos] == key:
                return self.data[pos]
            else:
                pos = self.rehash(pos, len(self.slots))
                if pos == start:
                    return None
        return None

    def __getitem__(self, key):
        # Get item using []
        return self.get(key)

    def __setitem__(self, key, data):
        # Set item using []
        self.put(key, data)

if __name__ == '__main__':
    h = HashTable()
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'
    print(h.slots)
    print(h.data)

    print(h[20])
    print(h[17])
    h[20] = 'duck'
    print(h[20])
    print(h[99])
    print(h.data)
