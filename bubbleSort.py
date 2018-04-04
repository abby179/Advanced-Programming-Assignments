from sortarray import *


def bubbleSort(sa):
    exchanges = True
    passnum = sa.getSize() - 1

    while passnum > 0 and exchanges:
        exchanges = False

        for i in range(passnum):
            if sa.cmp(i, i + 1) > 0:
                exchanges = True
                sa.swap(i, i + 1)
        passnum = passnum - 1


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

        bubbleSort(sa)

        if debug:
            print("after: ")
            sa.printList()

        sa.printInfo()

    print()











