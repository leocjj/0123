#!/usr/bin/python3
"""
Solve the Tower of Hanoi problem
"""


def move_tower(height, from_pole, to_pole, with_pole):
    # Move all the disks from one pole to another
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(from_pole, to_pole):
    # Move a disk from one pole to another
    print('moving disk from', from_pole, 'to', to_pole)

if __name__ == '__main__':
    move_tower(5, 'A', 'B', 'C')
