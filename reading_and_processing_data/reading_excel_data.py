import pandas as pd
import warnings

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    file_path = r'C:\Users\Lenovo\Desktop\GDT_Polish_Validation\Survey_Data.xlsx'
    raw_data = pd.read_excel(file_path, engine="openpyxl")
