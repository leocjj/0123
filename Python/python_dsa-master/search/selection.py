#!/usr/bin/python3
# Implement selection sort
# O(n^2)


def selection_sort(my_list):
    # Implement selection sort
    for passes in range(len(my_list) - 1, 0, -1):
        pos_max = 0
        for i in range(1, passes + 1):
            if my_list[i] > my_list[pos_max]:
                pos_max = i
        my_list[passes], my_list[pos_max] = my_list[pos_max], my_list[passes]
        print(my_list)


if __name__ == '__main__':
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(my_list)
    selection_sort(my_list)
