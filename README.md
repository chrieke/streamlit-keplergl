# streamlit-keplergl

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/chrieke/streamlit-keplergl/main/examples/streamlit-keplergl-example.py)
[![PyPi](https://img.shields.io/pypi/v/streamlit-keplergl)](https://pypi.org/project/streamlit-keplergl/)

**🗾 Streamlit component for rendering [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter#2-add-data) maps
in a streamlit app.**

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

## Usage

```python
import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

st.write("This is a kepler.gl map in streamlit")

map_1 = KeplerGl()
keplergl_static(map_1)
```

**Use within a streamlit column etc:**
```python
col1 = st.column(1)
with col1:
  keplergl_static(map_1)
```

**Set map location:**

The initial map location is configured via the KeplerGL object configuration, see
[example](https://github.com/chrieke/streamlit-keplergl/issues/4#issuecomment-1011207633). If your map contains data
you can use the `center_map` parameter, see below.


## Parameters:
- **fig**: `keplergl.KeplerGl` map figure.
- **height**: Fixed pixel height of the map. Optional, might result in non-optimal layout on some devices. By
  default the map height is determined by the keplergl figure height.
- **width**: Fixed pixel width of the map. Optional, by default the map width adjusts to the streamlit layout.
- **center_map**: Centers the map on the current map data, default False.
- **read_only**: Disables the side panel for map customization, default False.


## More infos

Also see the [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter#2-add-data) documentation
for general info on usage of kepler.gl in Python.
