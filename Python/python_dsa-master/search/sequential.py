#!/usr/bin/python3
# Implement sequential search
# O(n)


def sequential_search(my_list, item):
    # Implement sequential search
    for i in range(len(my_list)):
        if my_list[i] == item:
            return True
    return False


def ordered_sequential_search(my_list, item):
    # Implement ordered sequential search
    for i in range(len(my_list)):
        if my_list[i] == item:
            return True
        elif my_list[i] > item:
            return False
    return False

if __name__ == '__main__':
    test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequential_search(test_list, 3))
    print(sequential_search(test_list, 13))
    ordered_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(ordered_sequential_search(ordered_list, 3))
    print(ordered_sequential_search(ordered_list, 13))
