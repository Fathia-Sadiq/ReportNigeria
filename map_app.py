import geopandas as gpd
import streamlit as st
import folium
import mapclassify
from matplotlib import pyplot as plt

#file type must be .shp
file = gpd.read_file('nga_admin_boundaries.shp/nga_admin2.shp')
print(file.columns)

file.head()
m = file.explore('adm1_name',tooltip=False, popup=['adm2_name','adm1_name', 'area_sqkm','adm2_ref_n','sendist_en','center_lat','center_lon'])
m.save("map.html")
import webbrowser
webbrowser.open("map.html")