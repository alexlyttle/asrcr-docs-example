Generating API
--------------

You now have some documentation and code. However, you may want to provide
an API (application programming interface) to some code you have been
working on. There are several ways to
do this, but this guide focuses on Sphinx extensions. Alternatively,
you can use third-party extensions such as
`Sphinx AutoAPI <https://sphinx-autoapi.readthedocs.io/en/latest/>`_.

Sphinx has tools for automatically generating API documentation. One
example of this is the ``autodoc`` extension. Here is an example for
how to use it.

Add the following extensions to ``docs/conf.py``.

.. code-block:: python
    :caption: conf.py

    extensions = [
        "sphinx.ext.autodoc",
    ]

Preemptively add the API file to your TOC in ``docs/index.rst``,

.. code-block:: rst
    :caption: index.rst

    .. toctree::
       :maxdepth: 2
       :caption: Contents:
        
       publish
       adding-code
       api  .. <-- add this

Now create the file ``docs/api.rst`` to contain your API,

.. code-block:: rst
    :caption: api.rst

    API
    ===

    .. toctree::
       :caption: Packages:

       <your-package>

You can get creative here, but I suggest adding your packages,
subpackages, and submodules to a TOC in the API file. Then, for
each package, subpackage, and submodule, create a new RST file.

.. code-block:: rst
    :caption: <your-package>.rst

    <your-package>
    ==============

    .. toctree::
       :caption: Submodules:

       <your-package>.<your-submodule>

    .. automodule:: <your-package>
       :members:

Here, we create a TOC for any submodules in the package (you may
create a separate TOC for subpackages etc.) and then follow it with
``.. automodule::`` to generate documentation for
``<your-package>/__init__.py``.

Then, do the same recursively for subpackages and submodules, e.g.

.. code-block:: rst
    :caption: <your-package>.<your-submodule>.rst

    <your-package>.<your-submodule>
    ===============================

    .. automodule:: <your-package>.<your-submodule>
       :members:

Then, clean and build the documentation,

.. code-block::

   make clean; make html

Sphinx will automatically import your package(s) and create documentation
from the docstrings.

.. note::
   
   You will need to write docstrings in reStructuredText format, or see
   the next chapter.
