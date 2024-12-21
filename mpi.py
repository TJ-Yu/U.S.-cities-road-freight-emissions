# -*- coding: utf-8 -*-
"""
Code for processing and analyzing census data with weighted distance calculations for ethnicities.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def load_data(file_path, dtype=None):
    """Load Excel data into a DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.read_excel(file_path, dtype=dtype)

def standardize_column(df, column_name):
    """Standardize a column in the DataFrame."""
    scaler = StandardScaler()
    df[column_name + '_STD'] = scaler.fit_transform(df[[column_name]])
    return df

def normalize_column(df, column_name):
    """Normalize a column by dividing it by its max value."""
    df[column_name + '_NORM'] = df[column_name] / df[column_name].max()
    return df

def apply_weighted_dis(df, year, ethnicity_cols):
    """Apply distance-weighted calculations for ethnicity columns."""
    for col in ethnicity_cols:
        df[f'{col}DisWeighted{year}'] = (df['NEAR_DIST_NORM'].max() - df['NEAR_DIST_NORM']) * df[f'{col}{year}']
    return df

def calculate_changes(df):
    """Calculate the changes for each ethnicity group between 2011 and 2020."""
    for col in ['Minority', 'Black', 'Asian', 'Native', 'Hispanic']:
        df[f'{col}Change'] = df[f'{col}DisWeighted20'] - df[f'{col}DisWeighted11']
    return df

def filter_and_group(df, filter_column, group_columns, agg_columns):
    """Filter DataFrame by a column and group by 'CountyID'."""
    filtered_df = df[df[filter_column] == 1]
    grouped_df = filtered_df.groupby('CountyID')[agg_columns].agg('mean').reset_index()
    return grouped_df

def save_to_excel(df, file_path):
    """Save DataFrame to an Excel file."""
    df.to_excel(file_path, index=False, sheet_name='ProcessedData')

def main():
    # File paths
    input_file_path = 'data/census_data_with_county_type.xlsx'  # Input data file path
    ethnicity_file_path = 'data/ethnicity_data.xlsx'  # Ethnicity data file path
    output_file_path = 'output/processed_census_data.xlsx'  # Final processed data

    # Load data
    df = load_data(input_file_path, dtype={'CountyID': str})
    ethnicity_df = load_data(ethnicity_file_path)

    # Merge the dataframes
    merged_df = pd.merge(df, ethnicity_df, on='GEOID', how='left')
    df = merged_df

    # Standardize and normalize NEAR_DIST
    df = standardize_column(df, 'NEAR_DIST')
    df = normalize_column(df, 'NEAR_DIST')

    # Ethnicity columns for the calculation
    ethnicity_cols = ["Minorpct", "Black", "Asian", "Native", "Hispanic"]

    # Apply distance-weighted calculations for both 2011 and 2020
    for year in ["11", "20"]:
        df = apply_weighted_dis(df, year, ethnicity_cols)

    # Calculate changes for each ethnicity group
    df = calculate_changes(df)

    # Filter by "Gateway" category and perform grouping
    gateway_grouped_df = filter_and_group(df, 'GatewayDummy',
                                          ['MinorityDisWeighted11', 'MinorityDisWeighted20', 'MinorityChange',
                                           'BlackDisWeighted11', 'BlackDisWeighted20', 'BlackChange',
                                           'AsianDisWeighted11', 'AsianDisWeighted20', 'AsianChange',
                                           'NativeDisWeighted11', 'NativeDisWeighted20', 'NativeChange',
                                           'HispanicDisWeighted11', 'HispanicDisWeighted20', 'HispanicChange'])

    # Output the results to Excel
    save_to_excel(df, output_file_path)
    save_to_excel(gateway_grouped_df, 'output/gateway_grouped_data.xlsx')

    print("Processing completed successfully.")

# Run the main function
if __name__ == "__main__":
    main()
