import pandas as pd

# This function helps to limit the result only to columns with zero values per dataset
def show_zero_columns(df, df_name="Dataset"):
    zero_counts = (df == 0).sum()
    zero_percent = ((df == 0).mean() * 100)

    zero_summary = pd.DataFrame({
        "zero_count": zero_counts,
        "zero_percent": zero_percent
    })

    zero_summary = zero_summary[zero_summary['zero_count'] > 0]  # Columns with null values only
    zero_summary = zero_summary.sort_values('zero_count', ascending=False)  # Sort by highest null

    print(f"\nColumns with zero values in {df_name}:")
    if zero_summary.empty:
        print("No zero values found")
    else:
        print(zero_summary)