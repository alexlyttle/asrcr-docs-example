Extras
======

Here are some cool things you can add to your docs.

Theme
-----

Sphinx comes with `builtin themes <https://www.sphinx-doc.org/en/master/usage/theming.html>`_.
This documentation uses the `Sphinx Book Theme <https://sphinx-book-theme.readthedocs.io/en/stable/>`_.

1. Add the theme to the requirements and install it,

   .. code-block::

      echo sphinx-book-theme >> docs/requirements.txt
      pip install sphinx-book-theme

2. Go to the ``conf.py`` file and add the following lines,

   .. code-block::

      html_theme = 'sphinx_book_theme'

This theme allows you to add hyperlinks to the source repository and more.

Math
----

Render math using the ``mathjax`` extension.


.. code-block:: python
    :caption: conf.py

    extensions = [
        ...,
        'sphinx.ext.mathjax',
    ]

Here is an example,

.. math::

    f(x) = \int_0^\infty x^2 \, dx

Generate notebooks
------------------

Use the ``nbsphinx`` extension to automatrically generate documentation
from Jupyter notebooks.

Intersphinx
-----------

Reference external documentation in your docstrings using the
``intersphinx`` extension.
