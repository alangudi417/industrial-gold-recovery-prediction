import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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