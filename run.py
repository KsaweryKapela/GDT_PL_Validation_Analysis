from GDT_PL_Validation_Statistics.reading_and_processing_data.populating_data_class import Data
from GDT_PL_Validation_Statistics.reading_and_processing_data.reading_excel_data import raw_data
from GDT_PL_Validation_Statistics.statistics.statistics import r_pearson, shapiro_wilk
from GDT_PL_Validation_Statistics.visualization.bar_graphs import bar_graph

data = Data(raw_data)

r_pearson(data.IGD_20.scores(), data.GDT.scores())
bar_graph(data.GDT.scores())
shapiro_wilk(data.GDT.scores())
