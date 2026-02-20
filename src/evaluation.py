import pandas as pd
import numpy as np

# Function to calculate recovery
def calculate_rougher_recovery(df):
    """
    Calculate recovery:
    Recovery = (C × (F - T)) / (F × (C - T)) × 100

    Where:
    C = Gold concentration in the rougher concentrate (rougher.output.concentrate_au)
    F = Gold concentration in the feed (rougher.input.feed_au)
    T = Gold concentration in the rougher tailings (rougher.output.tail_au)
    """
    C = df['rougher.output.concentrate_au']
    F = df['rougher.input.feed_au']
    T = df['rougher.output.tail_au']
    
    # Apply metallurgical recovery formula
    recovery = (C * (F - T)) / (F * (C - T)) * 100
    return recovery

