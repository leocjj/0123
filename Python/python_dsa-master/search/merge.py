#!/usr/bin/python3
# Implement merge sort
# O(nlog(n))


def merge_sort(my_list):
    # Implement merge sort
    print('Splitting', my_list)
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1
        print('Merging', my_list)


if __name__ == '__main__':
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(my_list)
    merge_sort(my_list)
    print(my_list)
