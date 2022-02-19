from typing import Optional

import streamlit.components.v1 as components
from keplergl import KeplerGl


def keplergl_static(
    fig: KeplerGl, height: Optional[int] = None, width: Optional[int] = None, **kwargs
) -> components.html:
    """
    Renders `keplergl.KeplerGl` map figure in a Streamlit app. This method is
    a static Streamlit Component, meaning, no information is passed back from
    KeplerGL on browser interaction.

    Args:
        fig: `keplergl.KeplerGl` map figure.
        height: Fixed pixel height of the map, optional. By default determined by the height
            setting of the KeplerGl.keplergl figure object.
        width: Fixed pixel width of the map, optional. By default the width of the map adjusts
            to the streamlit layout option, e.g. also when used inside a column or container etc.
        kwargs: Add any argument of KeplerGl.save_to_html() (data, config, read_only).

    Example:
        ```python
            >>> map_1 = KeplerGl()
            >>> keplergl_static(map_1)
        ```
    """
    try:
        html = fig._repr_html_(kwargs)
    except AttributeError:
        raise TypeError("fig argument has to be a keplergl map object of type keplergl.KeplerGl!")

    if height is None:
        height = fig.height
    return components.html(
        html, height=height + 10, width=width
    )
