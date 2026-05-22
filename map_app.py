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

incident = st.text_input("Enter location in this format (LGA, State): Ex: (Ifedore, Ondo State)")
def validate_data(inp: str) -> None:
    pattern = r"[a-zA ]+[,]+ [a-zA ]"
    if re.match(pattern, inp) == None:
        st.error("Invalid input: should be (LGA, State)")

st.button(
    "Validate data",
    type="primary",
    icon=":material/refresh:",
    on_click=validate_data,
    kwargs={"inp": incident},
)   

details = st.text_input("Please enter details of attack: Type of attack, number of deaths, etc")
srcs = st.text_input("Please add additional sources")
#file type must be .shp
file = gpd.read_file('nga_admin_boundaries.shp/nga_admin2.shp')


m = file.explore('adm1_name',tooltip=False, popup=['adm2_name','adm1_name', 'area_sqkm','adm2_ref_n','sendist_en','center_lat','center_lon'])
st_data = st_folium(m, use_container_width=True)
#st.write(st_data)
data = st_data["last_active_drawing"]
if data != None:
    ppties = data["properties"]
    lat = ppties["center_lat"]
    lon = ppties["center_lon"]
    st.write(lat, lon)
#st.write(data)