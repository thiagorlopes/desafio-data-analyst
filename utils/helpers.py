import pandas as pd
import numpy as np
import seaborn as sns

# Imprime valores únicos, exceto nulos, para uma dada série pandas
def print_unique(series):
    unique_values = np.unique(series.dropna())
    print("Total: ", len(unique_values))
    print(unique_values)

# Extrai os n primeiros itens para uma coluna específica do dataframe
def extract_top(df, n, column):
    return df.sort_values(by=column, ascending=False).head(n)

# Plota um gráfico de barras para um dado dataframe
def plot_bars(df, x, y):
    return sns.catplot(data=df, x=x, y=y, kind='bar', height=5, aspect=2)

# Insere valores acima de um gráfico de barras
def annotate_bars(g):
    for ax in g.axes.ravel():
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.2f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center',
                va = 'center',
                xytext = (0, 10),
                textcoords = 'offset points')