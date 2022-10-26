from pprint import pprint
import numpy as np
import pandas as pd
from factor_analyzer import (ConfirmatoryFactorAnalyzer, ModelSpecificationParser)
from GDT_PL_Validation_Statistics.reading_and_processing_data.populating_data_class import Data
from GDT_PL_Validation_Statistics.reading_and_processing_data.reading_excel_data import raw_data

data = Data(raw_data)

cfa_dict = {'Q_1': data.GDT.q_1,
            'Q_2': data.GDT.q_2,
            'Q_3': data.GDT.q_3,
            'Q_4': data.GDT.q_4,
            'Sex': data.personal_data.sex,
            'Age': data.personal_data.age,
            'Weekly': data.gaming_habits.weekly_hours}

cfa_df = pd.DataFrame(cfa_dict)

print(np.array(cfa_dict.values()).shape)
model_dict = {"F1": ["V1", "V2", "V3", "V4", 'V5', 'V6', 'V7']}

model_spec = ModelSpecificationParser.parse_model_specification_from_dict(cfa_dict, model_dict)

cfa = ConfirmatoryFactorAnalyzer(model_spec, disp=False)

cfa.fit(cfa_df.values)

pprint(cfa.loadings_)
