import geopandas as gpd
import streamlit as st
import folium
from streamlit_folium import st_folium
import mapclassify
from matplotlib import pyplot as plt
import re

st.title("ReportNigeria")
st.write("This Web app displays all reported terrorist attacks happening all over the country")
st.write("\nReport an Incident:\n")

#file type must be .shp
file = gpd.read_file('nga_admin_boundaries.shp/nga_admin2.shp')
#Extracting LGA (adm2_name)
lga = file['adm2_name'].unique()
lga_option = st.selectbox(
   "Select LGA:",
   lga,
   index=None,
   placeholder="Enter the affected LGA",
)
# Displaying the selected option
st.write("You selected:", lga_option)
#Extracting State (adm1_name)
state = file['adm1_name'].unique()
state_option = st.selectbox(
   "Select State:",
   state,
   index=None,
   placeholder="Enter the affected State",
)
# Displaying the selected option
st.write("You selected:", state_option)

#filter and confirm that LGA belongs to the selected State
confirm_inp = file[(file['adm2_name'] == lga_option) & (file['adm1_name'] == state_option)]
if confirm_inp.empty:
    st.error("The selected LGA does not belong to the selected State.")
else:
    details = st.text_input("Please enter details of attack: Type of attack, number of deaths, etc")
    srcs = st.text_input("Please add additional sources")

m = file.explore('adm1_name',tooltip=False, popup=['adm2_name','adm1_name', 'area_sqkm','sendist_en','center_lat','center_lon'])
st_data = st_folium(m, use_container_width=True)
#st.write(st_data)
data = st_data["last_active_drawing"]
if data != None:
    ppties = data["properties"]
    lat = ppties["center_lat"]
    lon = ppties["center_lon"]
    st.write(lat, lon)
#st.write(data)
