# Welcome to Dask Sphinx Theme's documentation!

```{toctree}
:maxdepth: 2
:hidden:

demo
```

This is the official Sphinx theme for Dask documentation. It extends the
[PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html), 
but adds custom styling and a navigation bar to additional Dask subprojects.

## Installation

```bash
pip install dask-sphinx-theme

# or

conda install -c conda-forge dask-sphinx-theme
```

# Configuration

When creating a Dask subproject you can include this theme by changing this
line in your `conf.py` file

```python
# conf.py
html_theme = 'dask_sphinx_theme'
```

And by including `dask-sphinx-theme` as a requirement in your documentation
installation.
