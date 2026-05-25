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
   index=0,
   placeholder="Enter the affected LGA",
)
# Displaying the selected option
st.write("You selected:", lga_option)
#Extracting State (adm1_name)
state = file['adm1_name'].unique()
state_option = st.selectbox(
   "Select State:",
   state,
   index=0,
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
    uploaded_files = st.file_uploader("Please add additional sources (Valid file types: pdf, docx, jpg, png)",
                                       accept_multiple_files=True, 
                                       type=['pdf', 'docx', 'jpg', 'png'])

#extract the coordinates of the selected LGA and display on map
try:
    lon = confirm_inp['center_lon'].values[0]
    lat = confirm_inp['center_lat'].values[0]
except IndexError:
    st.error("Coordinates not found for the selected LGA.")
#st.write("Coordinates of the selected LGA:", lat, lon)
m = file.explore('adm1_name',tooltip=False, popup=['adm2_name','adm1_name', 'area_sqkm','sendist_en','center_lat','center_lon'])
#add a marker to the map
try:
    folium.Marker([lat, lon], icon=folium.Icon(color='red')).add_to(m)
except:
    st.write("")
st_data = st_folium(m, use_container_width=True)

