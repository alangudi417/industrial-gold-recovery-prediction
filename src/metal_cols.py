import pandas as pd
import numpy as np

def clear_metal_columns(df, metals=('au', 'ag', 'pb')):
    """
    This function identifies metal-related columns and replaces zero values with NaN.

    Parameters:
        Input dataframe
        metals: Metal keywords to search in column names

    Returns:
        Cleaned dataframe
        List of identified metal columns with replaced zeros with null values
    """

    # Identify metal concentration columns
    metal_columns = [
        col for col in df.columns
        if any(metal in col.lower() for metal in metals)
    ]

    print("Metal-related columns found:")
    for col in metal_columns:
        print(f"- {col}")

    return df, metal_columns
