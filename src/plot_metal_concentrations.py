import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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