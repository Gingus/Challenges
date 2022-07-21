def index_all(search_list, item):
    """Search lists and lists within, for item"""
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):
                indices.append([i]+index)
    return indices

#  Write a python function to index all items in a list
#  Input values (list to search, value to search for)
#  Output = a list of indices, each represented by a list of numbers
#  don't forget that lists can contain other lists
