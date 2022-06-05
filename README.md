# streamlit-keplergl

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/chrieke/streamlit-keplergl/main/examples/streamlit-keplergl-example.py)
[![PyPi](https://img.shields.io/pypi/v/streamlit-keplergl)](https://pypi.org/project/streamlit-keplergl/)

**🗾 Streamlit Component for rendering [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter#2-add-data) maps in a streamlit app.**

---

<h3 align="center">
  🎈 <a href="https://share.streamlit.io/chrieke/streamlit-keplergl/main/examples/streamlit-keplergl-example.py">Live Demo</a> 🎈
</h3>

---

<p align="center">
    <img src="./examples/example-screenshot.png" width=700></a>
</p>

## Installation

```bash
pip install streamlit-keplergl
```

## How to use it

```python
import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

st.write("This is a kepler.gl map in streamlit")

map_1 = KeplerGl()
keplergl_static(map_1)
```

**Parameters:**
- **fig**: `keplergl.KeplerGl` map figure.
- **height**: Fixed pixel height of the map, optional. By default determined by the height setting of the KeplerGl.
  keplergl figure object. Setting width and height explcitly might result in non optimal layout on other devices.
- **width**: Fixed pixel width of the map, optional. By default the adjusts to the streamlit layout option, e.g. 
  automatically adjusted to streamlit column or container width.
- **center_map**: The bound of the map will be centered on the current map data, default False.
- **read_only**: Hide side panel to disable map customization, default False.


To use the map widget within a streamlit column or other object:
```python
col1 = st.column(1)
with col1:
   keplergl_static(map_1)
```

Also see the [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter#2-add-data) documentation
for general info on usage of kepler.gl in Python.

## Adjust initial map location

To adjust the default initial map location (San Franciso), use the KeplerGL object configuration, 
see [here](https://github.com/chrieke/streamlit-keplergl/issues/4#issuecomment-1011207633).

