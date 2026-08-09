import pytest
import streamlit as st
from keplergl import KeplerGl

import streamlit_keplergl
from streamlit_keplergl import keplergl_static


@pytest.fixture
def iframe_calls(monkeypatch):
    """Captures the arguments passed to `st.iframe`."""
    calls = []
    monkeypatch.setattr(
        st,
        "iframe",
        lambda src, **kwargs: calls.append({"html": src, **kwargs}),
        raising=False,
    )
    return calls


@pytest.fixture
def html_calls(monkeypatch):
    """Captures `st.components.v1.html` calls, with `st.iframe` unavailable."""
    monkeypatch.delattr(st, "iframe", raising=False)
    calls = []
    monkeypatch.setattr(
        streamlit_keplergl.components,
        "html",
        lambda html, **kwargs: calls.append({"html": html, **kwargs}),
    )
    return calls


def test_renders_map_with_figure_height(iframe_calls):
    keplergl_static(KeplerGl(height=400))

    assert len(iframe_calls) == 1
    call = iframe_calls[0]
    assert call["height"] == 410
    assert call["width"] == "stretch"


def test_decodes_keplergl_bytes_to_str(iframe_calls):
    """keplergl returns utf-8 bytes, but streamlit expects a str."""
    keplergl_static(KeplerGl(height=400))

    html = iframe_calls[0]["html"]
    assert isinstance(html, str)
    assert "kepler" in html.lower()


def test_explicit_height_and_width_override_figure(iframe_calls):
    keplergl_static(KeplerGl(height=400), height=600, width=800)

    assert iframe_calls[0]["height"] == 610
    assert iframe_calls[0]["width"] == 800


def test_falls_back_to_components_html_without_st_iframe(html_calls):
    """Older streamlit versions have no `st.iframe`."""
    keplergl_static(KeplerGl(height=400), width=800)

    assert len(html_calls) == 1
    assert html_calls[0]["height"] == 410
    assert html_calls[0]["width"] == 800


def test_passes_center_map_and_read_only_to_keplergl(iframe_calls, monkeypatch):
    """Guards against a signature change in the keplergl `_repr_html_` API."""
    fig = KeplerGl(height=400)
    received = {}
    original = fig._repr_html_

    def spy(**kwargs):
        received.update(kwargs)
        return original(**kwargs)

    monkeypatch.setattr(fig, "_repr_html_", spy)
    keplergl_static(fig, center_map=True, read_only=True)

    assert received == {"center_map": True, "read_only": True}


@pytest.mark.parametrize("fig", ["not a map", None, 42])
def test_raises_on_non_keplergl_figure(fig, iframe_calls):
    with pytest.raises(TypeError, match="keplergl.KeplerGl"):
        keplergl_static(fig)

    assert iframe_calls == []
