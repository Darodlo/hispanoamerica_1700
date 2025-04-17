
import streamlit as st
import json
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("Progresión de la conquista hispana en América (1492–1700)")

# Cargar zonas conquistadas
with open("zonas_conquista.geojson", "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

# Obtener años únicos ordenados
año_sel = st.slider("Selecciona un año", min_value=1492, max_value=1700, step=1)

# Crear mapa base
m = folium.Map(location=[10, -70], zoom_start=3, tiles="CartoDB positron")

# Filtrar zonas por año
for feature in geojson_data["features"]:
    año = feature["properties"]["año_conquista"]
    if año <= año_sel:
        folium.GeoJson(
            feature,
            tooltip=feature["properties"]["region"],
            style_function=lambda x: {
                "fillColor": "#ffcc00",
                "color": "black",
                "weight": 1,
                "fillOpacity": 0.6,
            }
        ).add_to(m)

st.markdown(f"### Zonas conquistadas hasta {año_sel}")
st_data = st_folium(m, width=1200, height=600)
