
import streamlit as st
import json
import os

st.title("Hispanoamérica 1492–1700")

with open("data/timeline.json", "r", encoding="utf-8") as f:
    eventos = json.load(f)

años = sorted(set(e["anio"] for e in eventos))
año_sel = st.slider("Selecciona un año", min_value=min(años), max_value=max(años), step=1)
eventos_año = [e for e in eventos if e["anio"] == año_sel]

st.subheader(f"Resumen del año {año_sel}")
if eventos_año:
    for ev in eventos_año:
        st.markdown(f"### {ev['conquistador']} — *{ev['region']}*")
        st.write(ev["evento"])

        img_path = f"assets/conquistadores/{ev['conquistador'].replace(' ', '_').lower()}.jpg"
        flag_path = f"assets/banderas/{ev['region'].replace(' ', '_').lower()}.png"
        if os.path.exists(img_path):
            st.image(img_path, caption=ev["conquistador"], width=200)
        if os.path.exists(flag_path):
            st.image(flag_path, caption=ev["region"], width=100)
else:
    st.info("No hay eventos registrados para este año.")
