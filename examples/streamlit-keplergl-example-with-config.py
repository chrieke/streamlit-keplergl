import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

st.write("This is a kepler.gl map with specified configuration in streamlit")

config = {
    "version": "v1",
    "config": {
        "mapState": {
            "bearing": 0,
            "latitude": 52.52,
            "longitude": 13.4,
            "pitch": 0,
            "zoom": 11,
        }
    },
}
map_1 = KeplerGl()
map_1.config = config

keplergl_static(map_1)
