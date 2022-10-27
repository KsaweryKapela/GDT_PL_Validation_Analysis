import pandas as pd
import pingouin as pg

from GDT_PL_Validation_Statistics.reading_and_processing_data.populating_data_class import Data
from GDT_PL_Validation_Statistics.reading_and_processing_data.reading_excel_data import raw_data
from GDT_PL_Validation_Statistics.statistics.helpers import delete_nan
from GDT_PL_Validation_Statistics.statistics.statistics import spearman, r_pearson, shapiro_wilk, normalize_log, \
    chi_square_GOF

data = Data(raw_data)


def normal_distribution_of_scores():
    print('GDT')
    shapiro_wilk(data.GDT.scores())

    print('\nGDT log transformation')
    shapiro_wilk(normalize_log(data.GDT.scores()))


def correlations_between_scores():
    print('\nGDT/IGD_20')
    r_pearson(data.GDT.scores(), data.IGD_20.scores())
    spearman(data.GDT.scores(), data.IGD_20.scores())

    print('\nGDT/IDGS9')
    r_pearson(data.GDT.scores(), data.IGD_20.scores())
    spearman(data.GDT.scores(), data.IGDS9_SF.scores())

    print('\nIGD_20/IDGS9')
    r_pearson(data.GDT.scores(), data.IGD_20.scores())
    spearman(data.IGD_20.scores(), data.IGDS9_SF.scores())


def correlation_between_gdt_items():
    print('\nGDT q1/GDT score')
    r_pearson(data.GDT.scores(), data.GDT.q_1)
    spearman(data.GDT.scores(), data.GDT.q_1)

    print('\nGDT q2/GDT score')
    r_pearson(data.GDT.scores(), data.GDT.q_2)
    spearman(data.GDT.scores(), data.GDT.q_2)

    print('\nGDT q3/GDT score')
    r_pearson(data.GDT.scores(), data.GDT.q_3)
    spearman(data.GDT.scores(), data.GDT.q_3)

    print('\nGDT q4/GDT score')
    r_pearson(data.GDT.scores(), data.GDT.q_4)
    spearman(data.GDT.scores(), data.GDT.q_4)


def gdt_cronbachs_alpha():
    gdt_df = pd.DataFrame({
            'Q1': data.GDT.q_1,
            'Q2': data.GDT.q_2,
            'Q3': data.GDT.q_3,
            'Q4': data.GDT.q_4,
            })

    raw_results = pg.cronbach_alpha(data=gdt_df)
    print(f'\nGDT cronbachs alpha\nValue: {raw_results[0]}, 95% confidence interval: {raw_results[1]}\n')


def get_chi_square():
    gdt_data = delete_nan(data.GDT.scores())
    expected_data = None
    result = chi_square_GOF(gdt_data, expected_data)


def run_all_tests():
    normal_distribution_of_scores()
    correlations_between_scores()
    correlation_between_gdt_items()
    gdt_cronbachs_alpha()


run_all_tests()
