import math
import matplotlib.pyplot as plt

def generate_boxplots(df, column, value_column, plots_per_row=3, yscale='log'):
    """
    Generates boxplots for each unique value in the specified column of a dataframe.
    This code was improved with the help of ChatGpt to take an intial code set and confirm changes to make it a functional module

    Parameters:
    - df: pandas DataFrame
    - column: str, the column to group by (e.g., 'RegEntity_Group')
    - value_column: str, the column to plot values for (e.g., 'Value')
    - plots_per_row: int, number of plots per row in the output
    - yscale: str, scale for the y-axis (e.g., 'log' or 'linear')
    
    Returns:
    - None (shows the plots)

    Example of code to use module:
    - generate_boxplots(df, column='RegEntity_Group', value_column='Value')
    """
    unique_groups = df[column].unique()

    # Calculate the required number of rows
    num_rows = math.ceil(len(unique_groups) / plots_per_row)

    # Create subplots
    fig, axes = plt.subplots(nrows=num_rows, ncols=plots_per_row, figsize=(18, 3 * num_rows))
    axes = axes.flatten()  # Flatten the axes array for easier indexing

    # Loop through each unique value in the column and corresponding axes
    for idx, group in enumerate(unique_groups):
        # Filter data for the current group
        group_data = df.loc[df[column] == group, value_column].dropna()

        # Create a boxplot for the current group
        axes[idx].boxplot(group_data, vert=True, patch_artist=True, labels=[group])

        # Add labels and title
        axes[idx].set_title(f'Boxplot of {value_column} for {group}')
        axes[idx].set_ylabel(value_column)
        axes[idx].set_xlabel(column)

    # Hide any unused axes
    for ax in axes[len(unique_groups):]:
        ax.set_visible(False)

    # Adjust layout and show plot
    plt.yscale(yscale)
    plt.tight_layout()
    plt.show()
