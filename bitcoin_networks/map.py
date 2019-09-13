#!/usr/bin/env python3
"""
A library for mapping information for Bitcoin spatial data.
"""

__author__ = "Joe Blankenship"
__version__ = "19.0.1"
__license__ = ""

#%%
import pandas as pd
import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
from shapely.geometry import Point


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
def csv_to_geodf(filename, lon_col, lat_col):
    """
    This function converts CSV with lat/lon data to shapefile
    """
    data_raw = pd.read_csv(filename)
    data_gdf = gpd.GeoDataFrame(
        data_raw,
        crs={'init': 'epsg:4326'},
        geometry=[Point(xy) for xy in zip(data_raw[lon_col], data_raw[lat_col])]
    )
    return data_gdf


#%%
def points_in_polygon(point_gdf, poly_gdf):
    """
    This function performs a count points in polygon operation.
    Thanks to kwinkunks for the initial outline (https://stackoverflow.com/questions/27606924/count-number-of-points-in-multipolygon-shapefile-using-python)
    """
    pts = point_gdf.copy()
    pts_in_polys = []
    for i, poly in poly_gdf.iterrows():
        pts_in_this_poly = []
        for j, pt in pts.iterrows():
            if poly.geometry.contains(pt.geometry):
                pts_in_this_poly.append(pt.geometry)
                pts = pts.drop([j])
        pts_in_polys.append(len(pts_in_this_poly))
    poly_gdf['numpoints'] = gpd.GeoSeries(pts_in_polys)
    return poly_gdf

#%%
'''
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
'''
