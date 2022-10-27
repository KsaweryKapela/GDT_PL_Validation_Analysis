import pandas as pd
from factor_analyzer import FactorAnalyzer
from matplotlib import pyplot as plt
from GDT_PL_Validation_Statistics.reading_and_processing_data.populating_data_class import Data
from GDT_PL_Validation_Statistics.reading_and_processing_data.reading_excel_data import raw_data


def FA(fa_dict_input):
    data = Data(raw_data)
    gdt_dict = fa_dict_input(data)

    gdt_df = pd.DataFrame(gdt_dict)
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
