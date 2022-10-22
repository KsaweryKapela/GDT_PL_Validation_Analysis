import collections


def generate_index_dict(column):
    column_dict = {}

    for item in column:
        if item in column_dict:
            column_dict[item] += 1
        else:
            column_dict[item] = 1

    ordered_column_dict = collections.OrderedDict(sorted(column_dict.items()))

    return ordered_column_dict
