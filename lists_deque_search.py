from timeit import default_timer as timer
from collections import deque


# alist represents dict1
def sequential_search(alist, word):
    for i, d_word in enumerate(alist):
        if d_word == word:
            return i
    return -1


def binary_search(alist, item):
    first = 0
    last = len(alist)-1

    while first <= last:
        midpoint = (first + last)//2
        if alist[midpoint] < item:
            first = midpoint + 1
        elif alist[midpoint] > item:
            last = midpoint - 1
        else:
            return midpoint
    return -1


def create_dict_list(file):
    dict_list = []
    with open(file, 'r') as f:
        for line in f:
            dict_list.append(line.strip())
    return dict_list


def create_dict_deque(file):
    dict_deque = deque()
    with open(file, 'r') as f:
        for line in f:
            dict_deque.append(line.strip())
    return dict_deque


if __name__ == "__main__":
    # list search
    # dict1_list = create_dict_list('dict1.txt')
    # deque search
    dict1_list = create_dict_deque('dict1.txt')
    dict2_list = create_dict_list('dict2.txt')
    start = timer()
    for i in dict2_list:
        # sequential search
        sequential_search(dict1_list, i)
        # binary search
        # binary_search(dict1_list, i)
    end = timer()
    print('time spend: {}'.format(end - start))


