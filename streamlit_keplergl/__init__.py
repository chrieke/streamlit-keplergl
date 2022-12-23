from typing import Optional

import streamlit.components.v1 as components
from keplergl import KeplerGl


def keplergl_static(
    fig: KeplerGl,
    height: Optional[int] = None,
    width: Optional[int] = None,
    center_map: Optional[bool] = False,
    read_only: Optional[bool] = False,
) -> components.html:
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
    try:
        html = fig._repr_html_(center_map=center_map, read_only=read_only)
    except AttributeError:
        raise TypeError(
            "fig argument has to be a keplergl map object of type keplergl.KeplerGl!"
        )

    if height is None:
        height = fig.height
    return components.html(html, height=height + 10, width=width)
