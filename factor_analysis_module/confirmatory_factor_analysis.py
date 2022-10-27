from pprint import pprint
import numpy as np
import pandas as pd
from factor_analyzer import (ConfirmatoryFactorAnalyzer, ModelSpecificationParser)
from GDT_PL_Validation_Statistics.reading_and_processing_data.populating_data_class import Data
from GDT_PL_Validation_Statistics.reading_and_processing_data.reading_excel_data import raw_data


def CFA(cfa_dict_input):
    data = Data(raw_data)
    cfa_dict = cfa_dict_input(data)

    cfa_df = pd.DataFrame(cfa_dict)
    model_dict = {"F1": ["V1", "V2", "V3", "V4"]}
    model_spec = ModelSpecificationParser.parse_model_specification_from_dict(cfa_dict, model_dict)
    cfa = ConfirmatoryFactorAnalyzer(model_spec, disp=False)
    cfa.fit(cfa_df.values)
    pprint(cfa.loadings_)
