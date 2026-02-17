import pandas as pd
import numpy as np

def missing_values_over_time(df, date_column, perc):
    """
    This function resamples the percent over the different time frequencies.
    Returning:
        full resampled data per frequency.
    """
    df = df.copy()
    frequencies = {
        'Daily': 'd',
        'Weekly': 'W',
        'Monthly': 'ME'
    }

    results = {}

    for label, freq in frequencies.items():
        result = (
            df.set_index(date_column)
            .resample(freq)[perc]
            .mean()
        )

        results[label] = result

    return results