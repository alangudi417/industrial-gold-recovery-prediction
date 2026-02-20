import pandas as pd

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