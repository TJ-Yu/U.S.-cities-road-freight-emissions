# -*- coding: utf-8 -*-
"""
Code to calculate Moran's I and Bivariate Moran's I for pollution data and demographic data.
"""

import geopandas as gpd
from moran_calculations.moran_i import calculate_morans_i
from moran_calculations.moran_bv import calculate_bivariate_morans_i

# Read the geographic data
gdf = gpd.read_file('path/shapefile.shp')

# Rename columns for clarity
gdf = gdf.rename(columns={"Native_Ame": "Native11", "Native_A_1": "Native14",
                           "Native_A_2": "Native17", "Native_A_3": "Native20"})

# List of pollutants to analyze
pollutants = ['PM10dens11', 'PM10dens14', 'PM10dens17', 'PM10dens20',
              'PM25dens11', 'PM25dens14', 'PM25dens17', 'PM25dens20',
              'COdens11', 'COdens14', 'COdens17', 'COdens20',
              'CO2dens11', 'CO2dens14', 'CO2dens17', 'CO2dens20',
              'NOxdens11', 'NOxdens14', 'NOxdens17', 'NOxdens20']

# Calculate Moran's I for each pollutant
moran_results = {}
for pollutant in pollutants:
    moran_results[pollutant] = calculate_morans_i(gdf, pollutant)

# Print the Moran's I results
for pollutant, results in moran_results.items():
    print(f"{pollutant}: Moran's I = {results['I']}, p-value = {results['p-value']}")

# List of demographic variables to analyze
demographic_vars = ['Black11', 'Asian11', 'Native11', 'Hispanic11',
                    'Black20', 'Asian20', 'Native20', 'Hispanic20']

# Calculate Bivariate Moran's I between pollutants and demographic variables
bivariate_results = {}
for pollutant in pollutants:
    for demographic_var in demographic_vars:
        bivariate_results[f"{pollutant} & {demographic_var}"] = \
            calculate_bivariate_morans_i(gdf, pollutant, demographic_var)

# Print the Bivariate Moran's I results
for pair, results in bivariate_results.items():
    print(f"Bivariate Moran's I ({pair}): I = {results['I']}, p-value = {results['p-value']}")
