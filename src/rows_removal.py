import pandas as pd

def remove_high_null(df, percent_column, threshold):
    """
    Removes rows whose percentage of missing values exceeds the given threshold.

    Parameters:
    df: DataFrame to be cleaned
    percent_column: percent of missing data along the row. 
    threshold: Maximum allowed percentage of missing values (default 30%)

    Returns:
    Clean DataFrame without rows containing excessive missing values
    """
    # Filter rows that do NOT exceed the threshold
    clean_df = df.loc[df[percent_column] <= threshold].copy()
    
    # Cleaning statistics
    rows_removed = len(df) - len(clean_df)
    
    print(" - Cleaning statistics:")
    print(f" - Original rows: {len(df):,}")
    print(f" - Removed rows: {rows_removed:,}")
    print(f" - Remaining rows: {len(clean_df):,}")
    print(f" - Percentage removed: {(rows_removed/len(df)*100):.2f}%")
    
    return clean_df