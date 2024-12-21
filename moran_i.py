# -*- coding: utf-8 -*-
"""
This module calculates Moran's I for a single variable.
"""

from esda.moran import Moran
from libpysal.weights import Queen

def calculate_morans_i(gdf, variable):
    """
    Calculate Moran's I for a given variable in the GeoDataFrame.

    Parameters:
    gdf : GeoDataFrame
        The GeoDataFrame containing spatial data.
    variable : str
        The name of the variable for which to calculate Moran's I.

    Returns:
    dict
        A dictionary containing Moran's I value and p-value.
    """
    w = Queen.from_dataframe(gdf)
    moran = Moran(gdf[variable], w)
    return {'I': moran.I, 'p-value': moran.p_sim}
