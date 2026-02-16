import pandas as pd
import numpy as np

# Implementation of the function to remove rows with more than 30% missing values
def remove_high_null(df, threshold=30):
    """
    Removes rows whose percentage of missing values exceeds the given threshold.

    Parameters:
    df: DataFrame to be cleaned
    threshold: Maximum allowed percentage of missing values (default 30%)

    Returns:
    Clean DataFrame without rows containing excessive missing values
    """
    # Calculate percentage of missing values per row
    null_percentage = df.isnull().mean(axis=1) * 100
    
    # Filter rows that do NOT exceed the threshold
    clean_df = df[null_percentage <= threshold].copy()
    
    # Cleaning statistics
    rows_removed = len(df) - len(clean_df)
    
    print(" - Cleaning statistics:")
    print(f" - Original rows: {len(df):,}")
    print(f" - Removed rows: {rows_removed:,}")
    print(f" - Remaining rows: {len(clean_df):,}")
    print(f" - Percentage removed: {(rows_removed/len(df)*100):.2f}%")
    
    return clean_df