#!/usr/bin/env python

from setuptools import setup
import dask_sphinx_theme

setup(name='dask_sphinx_theme',
      version=dask_sphinx_theme.__version__,
      url='https://github.com/dask/dask-sphinx-theme/',
      license='BSD',
      author='Dask Developers',
      description='Dask theme for Sphinx',
      long_description=open('README.rst').read(),
      zip_safe=False,
      packages=['dask_sphinx_theme'],
      package_data={'dask_sphinx_theme': [
          'theme.conf',
          '*.html',
          'static/css/*.css',
          'static/images/*.svg',
          'static/js/*.js',
          'static/font/*.*'
      ]},
      include_package_data=True,
      # http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
      entry_points = {
          'sphinx.html_themes': [
              'dask_sphinx_theme = dask_sphinx_theme',
          ]
      },
      install_requires=open('requirements.txt').read().strip().split('\n'),
)
