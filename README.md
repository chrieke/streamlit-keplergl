# streamlit-kepler.gl


[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/chrieke/streamlit-keplergl/examples/streamlit-keplergl-example.py)

This Streamlit Component renders [kepler.gl](https://github.com/keplergl/kepler.gl) map figures in a Streamlit app.

## Installation

```
pip install streamlit-keplergl
```

## Example

<p align="center">
    <img src="./example-screenshot.png" width=700></a>
</p>

```
import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

map_1 = KeplerGl(height=400)
keplergl_static(map_1)
```
