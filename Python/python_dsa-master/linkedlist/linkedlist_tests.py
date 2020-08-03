#!/usr/bin/python3
"""
Test LinkedList methods
"""
from linkedlist import LinkedList

if __name__ == '__main__':
    mylist = LinkedList()

    mylist.add(31)
    mylist.insert(0, 77)
    mylist.append(17)
    mylist.insert(3, 93)
    mylist.add(26)
    mylist.insert(2, 54)
    print(mylist)
    print('size is ' + str(mylist.size()))

    print('index of 31 is ' + str(mylist.index(31)))
    print('index of 77 is ' + str(mylist.index(77)))
    print('index of 17 is ' + str(mylist.index(17)))
    print('index of 93 is ' + str(mylist.index(93)))
    print('index of 26 is ' + str(mylist.index(26)))
    print('index of 54 is ' + str(mylist.index(54)))
    print('index of 100 is ' + str(mylist.index(100)))

    print('insert 95 at position 5')
    mylist.insert(5, 95)
    print(mylist)

    print('insert 50 at position 8')
    mylist.insert(8, 50)
    print(mylist)

    print('insert 50 at position 7')
    mylist.insert(7, 50)
    print(mylist)

    print('remove 54')
    mylist.remove(54)
    print(mylist)

    print('remove 100')
    mylist.remove(100)
    print(mylist)

    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
    print(mylist.pop())
    print(mylist)
