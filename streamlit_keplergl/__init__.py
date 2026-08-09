from typing import Optional

import streamlit as st
import streamlit.components.v1 as components
from keplergl import KeplerGl


def keplergl_static(
    fig: KeplerGl,
    height: Optional[int] = None,
    width: Optional[int] = None,
    center_map: bool = False,
    read_only: bool = False,
) -> None:
    """
    Renders a `keplergl.KeplerGl` map figure in a Streamlit app.

    This is a static Streamlit component, thus information from browser interaction can not be passed back from
    KeplerGL to Python.

    Args:
        fig: `keplergl.KeplerGl` map figure.
        height: Fixed pixel height of the map. Optional, might result in non-optimal layout on some devices. By
            default the map height is determined by the keplergl figure height.
        width: Fixed pixel width of the map. Optional, by default the map width adjusts to the streamlit layout.
        center_map: Centers the map on the current map data, default False.
        read_only: Disables the side panel for map customization, default False.

    Example:
        ```python
            >>> map_1 = KeplerGl()
            >>> keplergl_static(map_1)
        ```
    """
    if not isinstance(fig, KeplerGl):
        raise TypeError(
            "fig argument has to be a keplergl map object of type keplergl.KeplerGl!"
        )

    html = fig._repr_html_(center_map=center_map, read_only=read_only)
    if isinstance(html, bytes):  # keplergl returns utf-8 encoded bytes.
        html = html.decode("utf-8")

    if height is None:
        height = fig.height

    if hasattr(st, "iframe"):
        # `st.components.v1.html` is deprecated and scheduled for removal.
        st.iframe(html, height=height + 10, width="stretch" if width is None else width)
    else:
        components.html(html, height=height + 10, width=width)
