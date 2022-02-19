# streamlit-keplergl

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/chrieke/streamlit-keplergl/main/examples/streamlit-keplergl-example.py)
[![PyPi](https://img.shields.io/pypi/v/streamlit-keplergl)](https://pypi.org/project/streamlit-keplergl/)

**🗾 Streamlit Component for rendering [kepler.gl](https://github.com/keplergl/kepler.gl/tree/master/bindings/kepler.gl-jupyter) maps in a streamlit app.**

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
By default, the width of the map is determined by the streamlit layout (automatically 
adjusted when used inside a streamlit column or container). The height is determined by the KeplerGL setting.
This can be fixed to a specific pixel size via the `width` and `height` parameters of `keplergl_static`, 
however the size might then not be optimal when viewed on a different device or mobile.

```python
keplergl_static(map_1, height=400, width=500)
```

To use it within a streamlit column or other object:
```python
col1 = st.column(1)
with col1:
   keplergl_static(map_1)
```


