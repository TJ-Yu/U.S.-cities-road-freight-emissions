# -*- coding: utf-8 -*-
"""
This module calculates Bivariate Moran's I between two variables.
"""

from esda.moran import Moran_BV
from libpysal.weights import Queen

def calculate_bivariate_morans_i(gdf, variable1, variable2):
    """
    Calculate Bivariate Moran's I between two variables.

    Parameters:
    gdf : GeoDataFrame
        The GeoDataFrame containing spatial data.
    variable1 : str
        The name of the first variable.
    variable2 : str
        The name of the second variable.

    Returns:
    dict
        A dictionary containing Bivariate Moran's I value and p-value.
    """
    w = Queen.from_dataframe(gdf)
    moran_bv = Moran_BV(gdf[variable1], gdf[variable2], w)
    return {'I': moran_bv.I, 'p-value': moran_bv.p_sim}
