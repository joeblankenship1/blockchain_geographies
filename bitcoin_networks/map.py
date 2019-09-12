#!/usr/bin/env python3
"""
A library for mapping information for Bitcoin spatial data.
"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""

#%%
import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs


#%%
def create_cartogram(filename):
    """
    This function produces a cartogram map.
    """
    data_raw = gpd.read_file(filename)
    map = gplt.cartogram(data_raw,
                         projection=gcrs.Robinson(),
                         scale=data_raw['NUMPOINTS'],
                         hue=data_raw['NUMPOINTS'],
                         cmap='Reds',
                         k=5,
                         figsize=(30, 15)
                         )
    return map


#%%
'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
