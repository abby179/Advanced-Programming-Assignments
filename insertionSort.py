from sortarray import *
from timeit import default_timer as timer


def insertionSort(sa):
    for index in range(1, sa.getSize()):

        while index > 0 and sa.cmp(index - 1, index) > 0:
            sa.swap(index - 1, index)
            index = index - 1


debug = False

start = timer()

sa = SortArray()
for size in range(10, 51, 10):
    print("SIZE: ", size)

    for method in ["shuffle", "miniShuffle", "reverse"]:
        print("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print("before: ")
            sa.printList()

        insertionSort(sa)

        if debug:
            print("after: ")
            sa.printList()

        sa.printInfo()

    print()

end = timer()
print("time: ", end - start)
