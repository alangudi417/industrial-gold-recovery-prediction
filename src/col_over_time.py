import pandas as pd
import numpy as np

def missing_values_over_time(df, date_column, perc, threshold=30):
    """
    This function is resampling the DataFrame over different frequencies, and returns 
    the result where the average exceeds the proposed threshold

    Parameters:
        df: input
        date_column: name of the column
        freq: here is the resample frequency ('h', 'd', 'w', 'm')
        threshold: minimum value to accept
    """

    # Set the frequencies: 
    frequencies = {
        'Hourly':'h',
        'Daily':'d',
        'Weekly':'W',
        'Monthly':'ME'
    }

    results = {}

    for label, freq in frequencies.items():
        result = (
            df.set_index(date_column)
                .resample(freq)[perc]
                .mean()
                .round(2)
        )

        result = result.loc[result > threshold].sort_values(ascending=False)
    
        if not result.empty:
            results[label] = result

    return results