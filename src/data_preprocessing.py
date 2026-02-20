import pandas as pd
import numpy as np

# This function identifies the total concentration columns and organize them by process stage
def concentration_stages_cols(
        df,
        patterns=('rougher.input.feed', 'rougher.output.concentrate', 'final.output.concentrate'),
        exclude=('feed_rate', 'feed_size')
):
    """
    This function identifies the total concentration columns and organize them by process stage. 
    Parameters:
        df: Input dataframe
        patterns: Define concentration columns
        exclude: excluding from the selection

    Returns:
        concentration_stages: a dictionary organized by stages. 
    """

    concentration_cols = []

    # Here we identify the concentration columns:
    for col in df.columns:
        col_lower = col.lower()

        if any(pattern in col_lower for pattern in patterns) and not any(ex in col_lower for ex in exclude):
            concentration_cols.append(col)
    
    # Here we organize by process stage. We start with empty lists:
    concentration_stages = {
        'Raw Material':[],
        'Rougher Concentrate': [],
        'Final Concentrate': []
    }

    for col in concentration_cols:
        col_lower = col.lower()

        if 'rougher.input.feed' in col_lower:
            concentration_stages['Raw Material'].append(col)
        elif 'rougher.output' in col_lower:
            concentration_stages['Rougher Concentrate'].append(col)
        elif 'final.output' in col_lower:
            concentration_stages['Final Concentrate'].append(col)
    
    # Print results
    print("Organized columns:")
    for stage, cols in concentration_stages.items():
        print(f"\n{stage}")
        for col in cols:
            print(f" - {col}")
    
    return concentration_stages

# This function identifies metal-related columns and replaces zero values with NaN.
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

# This function will help to remove the rows where the total concentration equals zero
def remove_zero_total_concentration(df, stages_dict):
    """
    This function will help to remove the rows where the total concentration equals zero. 

    Parameters:
        df: Input dataframe
        stages_dict: dictionary with the stage names and their columns
    
    Returns:
        final dataframe with the zero-total concentration data removed.
    """
    initial_len = len(df)

    stage_name = {
        'Raw Material': 'total_raw_material',
        'Rougher Concentrate': 'total_rougher_concentrate',
        'Final Concentrate': 'total_final_concentrate'
    }

    total_cols = []

    # Adding total columns
    for stage, cols in stages_dict.items():
        if cols:  # avoid errors if list is empty
            total_col = stage_name.get(
                stage,
                f"total_{stage.lower().replace(' ', '_')}"
            )
            df[total_col] = df[cols].sum(axis=1)
            total_cols.append(total_col)

    # Removing rows where the total concentration equals zero
    if total_cols:
        df = df[(df[total_cols] > 0).all(axis=1)]

    removed = initial_len - len(df)
    print(f"Rows removed due to zero total concentration: {removed}")
    
    return df

# This function helps to add total concentration columns per stage. 
def columns_total_concentrations(df, concentration_stages):
    """
    This function helps to add total concentration columns per stage. 

    Parameters:
        df: input dataframe
        concentration_stages: result from function concentration_stages_gold

    Returns:
        updated dataframe with total concentration columns
    """
    stage_name = {
        'Raw Material':'total_raw_material',
        'Rougher Concentrate': 'total_rougher_concentrate',
        'Final Concentrate': 'total_final_concentrate'
    }

    for stage, columns in concentration_stages.items():
        if columns: 
            new_col_name = stage_name.get(stage, f"total_{stage.lower().replace(' ', '_')}")
            df[new_col_name] = df[columns].sum(axis=1)
    
    return df

# This function removes rows whose percentage of missing values exceeds the given threshold.
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


