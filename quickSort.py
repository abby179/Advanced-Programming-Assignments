from sortarray import *


def quickSort(sa):
    quickSortHelper(sa, 0, sa.getSize() - 1)


def quickSortHelper(sa, first, last):
    if first < last:
        splitpoint = partition(sa, first, last)

        quickSortHelper(sa, first, splitpoint - 1)
        quickSortHelper(sa, splitpoint + 1, last)


def partition(sa, first, last):
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and sa.cmp(leftmark, first) <= 0:
            leftmark = leftmark + 1

        while sa.cmp(rightmark, first) >= 0 and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            sa.swap(leftmark, rightmark)

    sa.swap(first, rightmark)

    return rightmark


debug = False

sa = SortArray()
for size in range(10, 51, 10):
    print("SIZE: ", size)

    for method in ["shuffle", "miniShuffle", "reverse"]:
        print("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print("before: ")
            sa.printList()

        quickSort(sa)

        if debug:
            print("after: ")
            sa.printList()

        sa.printInfo()

    print()
