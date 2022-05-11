Extras
======

Here are some cool things you can add to your docs.

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
