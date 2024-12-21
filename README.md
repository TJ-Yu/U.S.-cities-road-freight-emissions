# The Role of U.S. Cities in Exacerbating Nationwide Disparities in Road Freight Emissions

## Overview

This repository provides Python scripts for calculating **Moran's I**, **Bivariate Moran's I**, and **MPI indicators** related to the analysis of road freight emissions across U.S. cities.

- **Moran's I** is used to measure the spatial autocorrelation of a single variable, helping to identify clustering or dispersion patterns of road freight emissions.
- **Bivariate Moran's I** extends this analysis to examine the relationship between two variables—such as pollution levels and demographic characteristics—across space.
- **MPI indicators calculation** focuses on applying distance-weighted metrics to assess how ethnicity and other demographic factors correlate with road freight emissions across U.S. counties and urban areas.

## Key Features

- **Spatial Autocorrelation**: Calculate **Moran's I** and **Bivariate Moran's I** for analyzing road freight emissions and their relationship with demographic variables.
- **Geospatial Data Processing**: Utilize `GeoDataFrame` from `GeoPandas` to manage geospatial data.
- **Distance-weighted Analysis**: Apply distance-based weights to evaluate the impact of proximity to road freight sources on emissions levels across different demographics.
- **Aggregation**: Aggregate data at the county level to better understand the regional disparities in road freight emissions and their associated impacts on various communities.

## Requirements

To use this code, you need to install the following Python libraries:

- `pandas` - Data manipulation and analysis
- `geopandas` - Geospatial data processing
- `libpysal` - Spatial econometrics
- `esda` - Empirical Spatial Data Analysis
- `scikit-learn` - For data preprocessing (StandardScaler)
- `openpyxl` - For saving output to Excel

You can install the dependencies using `pip`:

```bash
pip install pandas geopandas libpysal esda scikit-learn openpyxl
