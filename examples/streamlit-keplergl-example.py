import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

map_1 = KeplerGl(height=400)
keplergl_static(map_1)
