from timeit import default_timer as timer
from lists_deque_search import create_dict_list


def create_dict_dictionary(file):
    dict_dict = {}
    with open(file, 'r') as f:
        i = 0
        for line in f:
            dict_dict[line.strip()] = i
            i += 1
    return dict_dict


def search_dictionary(adict, item):
    for key in adict:
        if key == item:
            return adict[key]
    else:
        return -1


if __name__ == "__main__":
    dict1_dict = create_dict_dictionary('dict1.txt')
    dict2_list = create_dict_list('dict2.txt')
    start = timer()
    for i in dict2_list:
        search_dictionary(dict1_dict, i)
    end = timer()
    print('time spend: {}'.format(end - start))








