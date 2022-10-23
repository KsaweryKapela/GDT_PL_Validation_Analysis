import pandas as pd


def delete_nan(column):
    for item in column[:]:
        if pd.isna(item):
            column.remove(item)
    return column


def delete_nan_two_columns(column_1, column_2):
    cleared_column_1 = []
    cleared_column_2 = []

    for index in range(len(column_1)):
        cut = False
        if pd.isna(column_1[index]):
            cut = True
        elif pd.isna(column_2[index]):
            cut = True

        if not cut:
            cleared_column_1.append(column_1[index])
            cleared_column_2.append(column_2[index])

    return cleared_column_1, cleared_column_2


def return_true_len(column):
    value = 0
    for item in column:
        if item is True:
            value += 1
    return value

