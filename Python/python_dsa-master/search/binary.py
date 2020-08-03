#!/usr/bin/python3
# Implement binary search
# O(log(n))


def binary_search(my_list, item):
    # Implement binary search
    first = 0
    last = len(my_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if my_list[mid] == item:
            return True
        elif my_list[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False


def binary_search_recursive(my_list, item):
    # Implement binary search recursively
    if len(my_list) == 0:
        return False
    mid = len(my_list) // 2
    if my_list[mid] == item:
        return True
    elif my_list[mid] > item:
        return binary_search_recursive(my_list[:mid], item)
    else:
        return binary_search_recursive(my_list[mid + 1:], item)

if __name__ == '__main__':
    ordered_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(ordered_list, 3))
    print(binary_search(ordered_list, 13))
    print(binary_search_recursive(ordered_list, 3))
    print(binary_search_recursive(ordered_list, 13))
