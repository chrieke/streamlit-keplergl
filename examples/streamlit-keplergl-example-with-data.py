import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import pandas as pd

df = pd.DataFrame(
    {
        "City": ["San Francisco", "San Jose"],
        "Latitude": [37.77, 37.33],
        "Longitude": [-122.43, -121.89],
    }
)

st.dataframe(df.head())

st.write("This is a kepler.gl map with data input in streamlit")

map_1 = KeplerGl(height=400)
map_1.add_data(
    data=df, name="cities"
)  # Alternative: KeplerGl(height=400, data={"name": df})

keplergl_static(map_1, center_map=True)
