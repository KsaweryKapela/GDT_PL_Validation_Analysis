from matplotlib import pyplot as plt

from GDT_PL_Validation_Statistics.statistics.helpers import delete_nan
from GDT_PL_Validation_Statistics.visualization.helpers import generate_index_dict


def bar_graph(raw_column):
    column = delete_nan(raw_column)

    column_dict = generate_index_dict(column)
    print(column_dict)
    value = list(column_dict.keys())
    people = list(column_dict.values())

    plt.bar(value, people, color='maroon',
            width=0.2)

    plt.xlabel("Values")
    plt.ylabel("People")

    plt.show()
