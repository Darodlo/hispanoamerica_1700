import streamlit as st
import json
import os
from PIL import UnidentifiedImageError

# Título
st.title("Hispanoamérica 1492–1700")

# Cargar eventos desde archivo
try:
    with open("data/timeline.json", "r", encoding="utf-8") as f:
        eventos = json.load(f)
except FileNotFoundError:
    st.error("❌ No se encontró el archivo 'data/timeline.json'.")
    st.stop()

# Controlar que haya eventos
if not eventos:
    st.warning("⚠️ No hay eventos disponibles en el archivo.")
    st.stop()

# Slider de años
años = sorted(set(e["anio"] for e in eventos))
año_sel = st.slider("Selecciona un año", min_value=min(años), max_value=max(años), step=1)

# Mostrar eventos del año
st.subheader(f"Resumen del año {año_sel}")
eventos_año = [e for e in eventos if e["anio"] == año_sel]

if eventos_año:
    for ev in eventos_año:
        st.markdown(f"### {ev['conquistador']} — *{ev['region']}*")
        st.write(ev["evento"])

        # Imagen del conquistador
        img_path = f"assets/conquistadores/{ev['conquistador'].replace(' ', '_').lower()}.jpg"
        if os.path.exists(img_path):
            try:
                st.image(img_path, caption=ev["conquistador"], width=200)
            except UnidentifiedImageError:
                st.warning(f"⚠️ No se pudo mostrar la imagen de {ev['conquistador']}.")

        # Bandera de la región
        flag_path = f"assets/banderas/{ev['region'].replace(' ', '_').lower()}.png"
        if os.path.exists(flag_path):
            try:
                st.image(flag_path, caption=ev["region"], width=100)
            except UnidentifiedImageError:
                st.warning(f"⚠️ No se pudo mostrar la bandera de {ev['region']}.")
else:
    st.info("ℹ️ No hay eventos registrados para este año.")
