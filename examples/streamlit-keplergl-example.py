import streamlit as st
from keplergl import KeplerGl

from streamlit_keplergl import keplergl_static

st.write("This is a kepler.gl map in streamlit")

map_1 = KeplerGl(height=400)
keplergl_static(map_1)
