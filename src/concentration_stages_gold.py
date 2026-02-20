import pandas as pd

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