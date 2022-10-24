from GDT_PL_Validation_Statistics.reading_and_processing_data.populating_data_class import Data
from GDT_PL_Validation_Statistics.reading_and_processing_data.reading_excel_data import raw_data
from GDT_PL_Validation_Statistics.statistics.helpers import return_true_len
from GDT_PL_Validation_Statistics.statistics.split_correlations import split_correlations_func, split_into_sex_data, \
    split_into_relationship_data, split_into_online
from statistics import *
import warnings

from GDT_PL_Validation_Statistics.statistics.statistics import r_pearson

warnings.filterwarnings('ignore')
warnings.simplefilter("ignore")

data = Data(raw_data)


def interesting_findings():
    print('Weekly hours and self assessed chance of addiction')
    split_correlations_func(data, split_into_sex_data,
                            data.gaming_habits.weekly_hours, data.gaming_habits.respondents_addiction)

    print('Weekly hours and self assessed chance of addiction')
    split_correlations_func(data, split_into_sex_data,
                            data.gaming_habits.weekly_hours, data.gaming_habits.friends_addiction)

    print('My addiction vs friends addiction correlation to GDT scores')
    r_pearson(data.GDT.scores(), data.gaming_habits.respondents_addiction)
    r_pearson(data.GDT.scores(), data.gaming_habits.friends_addiction)


