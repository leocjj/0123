#!/usr/bin/python3
# Implement quick sort
# O(nlog(n))


def quick_sort(my_list):
    # Implement quick sort
    quick_sort_helper(my_list, 0, len(my_list) - 1)


def quick_sort_helper(my_list, first, last):
    # Quick sort helper
    if first < last:
        split = partition(my_list, first, last)
        quick_sort_helper(my_list, first, split - 1)
        quick_sort_helper(my_list, split + 1, last)


def partition(my_list, first, last):
    # Partition list around a pivot point
    pivot = my_list[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and my_list[left] <= pivot:
            left += 1
        while my_list[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            my_list[left], my_list[right] = my_list[right], my_list[left]
            print(my_list)
    my_list[first], my_list[right] = my_list[right], my_list[first]
    print(my_list)
    return right

if __name__ == '__main__':
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(my_list)
    quick_sort(my_list)
