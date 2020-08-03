#!/usr/bin/python3
# Implement bubble sort
# O(n^2)


def bubble_sort(my_list):
    # Implement bubble sort
    for passes in range(len(my_list) - 1, 0, -1):
        for i in range(passes):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                print(my_list)


if __name__ == '__main__':
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(my_list)
    bubble_sort(my_list)
