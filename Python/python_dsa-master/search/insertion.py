#!/usr/bin/python3
# Implement insertion sort
# O(n^2)


def insertion_sort(my_list):
    # Implement selection sort
    for i in range(1, len(my_list)):
        current = my_list[i]
        pos = i
        while pos > 0 and my_list[pos - 1] > current:
            my_list[pos] = my_list[pos - 1]
            pos -= 1
        my_list[pos] = current
        print(my_list)


if __name__ == '__main__':
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(my_list)
    insertion_sort(my_list)
