import numpy as np
import pandas as pd
from scipy.stats import pearsonr, shapiro, spearmanr, chisquare, ttest_ind, mannwhitneyu, pointbiserialr
from GDT_PL_Validation_Statistics.statistics.helpers import delete_nan, delete_nan_two_columns


def r_pearson(column_1_raw, column_2_raw):
    column_1, column_2 = delete_nan_two_columns(column_1_raw, column_2_raw)

    result = pearsonr(column_1, column_2)
    print(result)


def shapiro_wilk(column_raw):
    column = delete_nan(column_raw)

    result = shapiro(column)
    print(result)


def spearman(column_1_raw, column_2_raw):
    column_1, column_2 = delete_nan_two_columns(column_1_raw, column_2_raw)

    result = spearmanr(column_1, column_2)
    print(result)


def t_test(column_1_raw, column_2_raw):
    # column_1, column_2 = delete_nan_two_columns(column_1_raw, column_2_raw)
    result = ttest_ind(column_1_raw, column_2_raw)
    print(result)


def mann_whitney(column_1_raw, column_2_raw):
    # column_1, column_2 = delete_nan_two_columns(column_1_raw, column_2_raw)
    result = mannwhitneyu(column_1_raw, column_2_raw)
    print(result)


def normalize_log(column_raw):
    column = delete_nan(column_raw)
    transformed_data = np.log(column)
    return list(transformed_data)


def r_point_biserial(bool_column_raw, int_column_raw):
    bool_column, int_column = delete_nan_two_columns(bool_column_raw, int_column_raw)

    result = pointbiserialr(bool_column, int_column)
    print(result)


def chi_square_GOF(column_raw, expected):
    column = delete_nan(column_raw)
    result = chisquare(f_obs=column, f_exp=expected)
    print(result)

