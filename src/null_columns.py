import pandas as pd

# This function helps to limit the result only to columns with null values per dataset
def show_null_columns(df, df_name="Dataset"):
    null_counts = df.isnull().sum()
    null_percent = (df.isnull().mean() * 100)

    null_summary = pd.DataFrame({
        "null_count": null_counts,
        "null_percent": null_percent
    })

    null_summary = null_summary[null_summary['null_count'] > 0]  # Columns with null values only
    null_summary = null_summary.sort_values('null_count', ascending=False)  # Sort by highest null

    print(f"\nColumns with null values in {df_name}:")
    if null_summary.empty:
        print("No null values found")
    else:
        print(null_summary)