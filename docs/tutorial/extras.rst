Extras
======

Here are some cool things you can add to your docs.

Theme
-----

Sphinx comes with `builtin themes <https://www.sphinx-doc.org/en/master/usage/theming.html>`_.
However, this documentation uses the third-party `Sphinx Book Theme <https://sphinx-book-theme.readthedocs.io/en/stable/>`_.

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

.. code-block:: reStructuredText

    .. math::

        f(x) = \int_0^\infty x^2 \, dx

which renders as,

.. math::

    f(x) = \int_0^\infty x^2 \, dx

Generate notebooks
------------------

Use the ``nbsphinx`` extension to automatically generate documentation
from Jupyter notebooks.

Intersphinx
-----------

Reference external documentation in your docstrings using the
``intersphinx`` extension.

Inline tabs
-----------

The `sphinx-inline-tabs <https://sphinx-inline-tabs.readthedocs.io/en/latest/index.html>`_
extension allows you to do things like this using the ``.. tab::`` directive,

.. tab:: One

    This is the first tab.

.. tab:: Two

    This is the second tab.

.. tab:: Three

    This is the third tab.


