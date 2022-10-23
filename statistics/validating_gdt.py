import pandas as pd
import pingouin as pg

from GDT_PL_Validation_Statistics.reading_and_processing_data.populating_data_class import Data
from GDT_PL_Validation_Statistics.reading_and_processing_data.reading_excel_data import raw_data
from GDT_PL_Validation_Statistics.statistics.statistics import spearman, r_pearson, shapiro_wilk, normalize_log

data = Data(raw_data)


def normal_distribution_of_scores():
    print('GDT')
    shapiro_wilk(data.GDT.scores())

    print('IGD_20')
    shapiro_wilk(data.IGD_20.scores())
    print('\n')

    print('IGDS9_SF')
    shapiro_wilk(data.IGDS9_SF.scores())
    print('\n')


def correlations_between_scores():
    print('GDT/IGD_20')
    r_pearson(data.GDT.scores(), data.IGD_20.scores())
    spearman(data.GDT.scores(), data.IGD_20.scores())
    print('\n')

    print('GDT/IDGS9')
    r_pearson(data.GDT.scores(), data.IGD_20.scores())
    spearman(data.GDT.scores(), data.IGDS9_SF.scores())
    print('\n')

    print('IGD_20/IDGS9')
    r_pearson(data.GDT.scores(), data.IGD_20.scores())
    spearman(data.IGD_20.scores(), data.IGDS9_SF.scores())
    print('\n')


def correlation_between_gdt_items():
    print('GDT q1/GDT score')
    r_pearson(data.GDT.scores(), data.GDT.q_1)
    spearman(data.GDT.scores(), data.GDT.q_1)
    print('\n')

    print('GDT q2/GDT score')
    r_pearson(data.GDT.scores(), data.GDT.q_2)
    spearman(data.GDT.scores(), data.GDT.q_2)
    print('\n')

    print('GDT q3/GDT score')
    r_pearson(data.GDT.scores(), data.GDT.q_3)
    spearman(data.GDT.scores(), data.GDT.q_3)
    print('\n')

    print('GDT q4/GDT score')
    r_pearson(data.GDT.scores(), data.GDT.q_4)
    spearman(data.GDT.scores(), data.GDT.q_4)
    print('\n')


def gdt_cronbachs_alpha():
    gdt_df = pd.DataFrame({
            'Q1': data.GDT.q_1,
            'Q2': data.GDT.q_2,
            'Q3': data.GDT.q_3,
            'Q4': data.GDT.q_4,
            })

    raw_results = pg.cronbach_alpha(data=gdt_df)
    print(f'GDT cronbachs alpha\nValue: {raw_results[0]}, 95% confidence interval: {raw_results[1]}\n')


def run_all_tests():
    normal_distribution_of_scores()
    correlations_between_scores()
    correlation_between_gdt_items()
    gdt_cronbachs_alpha()


print(data.personal_data.sex)
