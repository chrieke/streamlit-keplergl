import setuptools
from pathlib import Path

parent_dir = Path(__file__).resolve().parent

setuptools.setup(
    name="streamlit-keplergl",
    version="0.0.2",
    author="Christoph Rieke",
    author_email="",
    description="Streamlit Component for rendering kepler.gl maps",
    long_description=parent_dir.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/chrieke/streamlit-keplergl",
    license="MIT",
    packages=setuptools.find_packages(exclude=("tests", "docs", "examples")),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=parent_dir.joinpath("requirements.txt").read_text().splitlines(),
)
