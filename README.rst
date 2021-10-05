Dask Sphinx Theme
=================

This is the official Sphinx theme for Dask documentation.  It extends the
``sphinx-book-theme`` project, but adds custom styling and a navigation bar to
additional Dask subprojects.

When creating a Dask subproject you can include this theme by changing this
line in your conf.py file

.. code-block:: python

   html_theme = 'dask_sphinx_theme'

And by including ``dask_sphinx_theme`` as a requirement in your documentation
installation.

Releasing
---------

This project is configured to automatically push a new release to PyPI whenever
a git tag is pushed. For example, to release a new ``x.y.z`` version of
``dask-sphinx-theme``, checkout the commit you would like to release,
add a git tag, and push the tag to the ``main`` branch of the
``dask/dask-sphinx-theme`` repository:

.. code-block::

   $ git checkout <commit-hash>
   $ git tag -a x.y.z -m 'Version x.y.z'
   $ git push upstream main --tags
