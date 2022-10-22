def generate_index_dict(column):
    column_dict = {}

    for item in column:
        if item in column_dict:
            column_dict[item] += 1
        else:
            column_dict[item] = 1

    return column_dict
