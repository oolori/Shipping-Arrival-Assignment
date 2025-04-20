import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


    # As part int64of the explorative analysis we wanted to see the impact of "Product_importance" on the "Reached.on.Time_Y.N". We believe products with high importance shoudld be mostly delivered on time

def plot_crossbar(data, column_x, column_y):
    CrosstabResult=pd.crosstab(index=data[column_x],columns=data[column_y])
    CrosstabResult.plot.bar()
    plt.show()


def plot_piechart(data, column):
    counts = data[column].value_counts()
    plt.pie(counts, labels = counts.index, autopct ='% 1.1f %%')
    plt.show()