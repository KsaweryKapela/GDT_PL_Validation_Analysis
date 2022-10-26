import pandas as pd
from factor_analyzer import FactorAnalyzer
# Create a factor analyzer variable and perform factor analysis
from matplotlib import pyplot as plt
from GDT_PL_Validation_Statistics.reading_and_processing_data.populating_data_class import Data
from GDT_PL_Validation_Statistics.reading_and_processing_data.reading_excel_data import raw_data

data = Data(raw_data)
gdt_questions = {'Q_1': data.GDT.q_1,
                 'Q_2': data.GDT.q_2,
                 'Q_3': data.GDT.q_3,
                 'Q_4': data.GDT.q_4}

gdt_df = pd.DataFrame(gdt_questions)
fa = FactorAnalyzer(n_factors=1, rotation='varimax')
fa.fit(gdt_df)

loadings = fa.loadings_
ev, v = fa.get_eigenvalues()

x_values = range(1, gdt_df.shape[1] + 1)
plt.scatter(x_values, ev)
plt.plot(x_values, ev)
plt.title('Scree plot')
plt.xlabel('Factor')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

loadings_df = pd.DataFrame.from_records(loadings)
print(loadings_df)
