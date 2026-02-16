import pandas as pd
import numpy as np

def missing_values_over_time(df, threshold=30):
    """
    This function looks for the result where the average exceeds the proposed threshold

    Parameters:
        df: input
        threshold: minimum value to accept
    """

    null_percent = df.isnull().mean(axis=1) * 100
    results = (null_percent > threshold).sum()

    return results