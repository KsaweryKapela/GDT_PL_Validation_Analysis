import pandas as pd
from scipy.stats import pearsonr, shapiro, spearmanr

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
