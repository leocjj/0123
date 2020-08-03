#!/usr/bin/python3
# Implement shell sort
# Between O(n) and O(n^2)


def shell_sort(my_list):
    # Implement shell sort
    sublist_size = len(my_list) // 2
    while sublist_size > 0:
        for start in range(sublist_size):
            gap_insertion_sort(my_list, start, sublist_size)
        print('After increments of size', sublist_size,
              'the list is', my_list)
        sublist_size //= 2


def gap_insertion_sort(my_list, start, gap):
    # Perform insertion sort with given gap
    for i in range(start + gap, len(my_list), gap):
        current = my_list[i]
        pos = i
        while pos >= gap and my_list[pos - gap] > current:
            my_list[pos] = my_list[pos - gap]
            pos -= gap
        my_list[pos] = current


if __name__ == '__main__':
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(my_list)
    shell_sort(my_list)
