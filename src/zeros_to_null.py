import pandas as pd
import numpy as np

# Function to replace zeros with null values in selected columns for further analysis
def zeros_null(df, columns):
    df = df.copy()
    df[columns] = df[columns].replace(0, np.nan)
    return df