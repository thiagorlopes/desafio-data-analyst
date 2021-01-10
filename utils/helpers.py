import pandas as pd
import numpy as np

def print_unique(series):
    unique_values = np.unique(series.dropna())
    print("Total: ", len(unique_values))
    print(unique_values)
