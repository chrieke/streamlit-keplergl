# Changelog

## 0.4.0

- Renders via `st.iframe` on newer Streamlit versions, falls back to `st.components.v1.html`
- Raises a `TypeError` instead of failing obscurely when `fig` is not a `keplergl.KeplerGl` object
- Handles keplergl returning utf-8 encoded bytes
- Requires Python 3.10+
- Packaging moved to `pyproject.toml`, added tests and CI

## 0.3.0

- Adds `center_map` and `read_only` arguments
- Fixes issue of data not displayed in map

## 0.2.0

- Adjusts use of `width` and `height` parameters based on feedback e.g. https://github.com/chrieke/streamlit-keplergl/issues/3
- Removes forced defaults for `width` & `height` parameters
- `height` parameter now correctly supersedes the keplergl figure object setting
- Adds better explanation and more examples
- Removes st component `scrolling` parameter as had no effect

## 0.1.0

- Initial release
