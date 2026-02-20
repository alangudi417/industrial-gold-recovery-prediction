import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This function helps to limit the result only to columns with null values per dataset
def show_null_columns(df, df_name="Dataset"):
    null_counts = df.isnull().sum()
    null_percent = (df.isnull().mean() * 100).round(2)

    null_summary = pd.DataFrame({
        "null_count": null_counts,
        "null_percent": null_percent
    })

    null_summary = null_summary[null_summary['null_count'] > 0]  # Columns with null values only
    null_summary = null_summary.sort_values('null_count', ascending=False).head()  # Sort by highest null

    print(f"\nColumns with null values in {df_name}:")
    if null_summary.empty:
        print("No null values found")
    else:
        print(null_summary)

# This function helps to limit the result only to columns with zero values per dataset
def show_zero_columns(df, df_name="Dataset"):
    zero_counts = (df == 0).sum()
    zero_percent = ((df == 0).mean() * 100).round(2)

    zero_summary = pd.DataFrame({
        "zero_count": zero_counts,
        "zero_percent": zero_percent
    })

    zero_summary = zero_summary[zero_summary['zero_count'] > 0]  # Columns with null values only
    zero_summary = zero_summary.sort_values('zero_count', ascending=False).head()  # Sort by highest null

    print(f"\nColumns with zero values in {df_name}:")
    if zero_summary.empty:
        print("No zero values found")
    else:
        print(zero_summary)

# Function to replace zeros with null values in selected columns for further analysis
def zeros_null(df, columns):
    df = df.copy()
    df[columns] = df[columns].replace(0, np.nan)
    return df

# This function will help to plot missing percent over time
def plot_missing_result(result_dict):
    """
    This function will help to plot missing percent over time

    Parameter:
        result_dict: Dictionary {label:Series}
    """

    fig, axes = plt.subplots(1, len(result_dict), figsize=(12,6))
    axes = axes.flatten()

    for ax, (label, series) in zip(axes, result_dict.items()):
        ax.plot(series)
        ax.axhline(30)
        ax.set_title(f'{label}')
        ax.set_xlabel('date')
        ax.set_ylabel('Missing Percentage')
        ax.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

# This function computes and prints average metal concentrations by stage
def plot_avg_metal_conc(df, stages, metals=('au', 'ag', 'pb')):
    """
    Computes and prints average metal concentrations by stage,
    and plots their progression across stages.

    Parameters:
        df: Input dataframe
        stages: Dictionary with stage names as keys and list of columns as values
        metals: Tuple of metal keywords to analyze
    """

    # Compute average concentrations by stage
    average_concentrations = {}

    for stage, columns in stages.items():
        stage_means = df[columns].mean()

        for col in stage_means.index:
            metal = col.split('_')[-1].upper()

            if metal not in average_concentrations:
                average_concentrations[metal] = {}

            average_concentrations[metal][stage] = stage_means[col]

    avg_df = pd.DataFrame(average_concentrations).T
    print("\nAverage Metal Concentrations by Stage:")
    print()
    print(avg_df.round(2))

    # Create visualization
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.5))

    for i, metal in enumerate(metals):
        stage_names = []
        concentrations = []

        for stage, columns in stages.items():
            metal_col = [col for col in columns if metal in col][0]
            stage_names.append(stage.split()[0].strip())
            concentrations.append(df[metal_col].mean())

        axes[i].plot(stage_names, concentrations, marker='o', linewidth=2.5)
        axes[i].set_title(f'"{metal}" Concentration')
        axes[i].set_ylabel('Concentration')
        axes[i].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

# This function resamples the percent over the different time frequencies.
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


