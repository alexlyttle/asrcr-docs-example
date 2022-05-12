Generating API
==============

You now have some documentation and code. However, you may want to provide
an API (application programming interface) to some code you have been
working on. There are several ways to
do this, but this guide focuses on Sphinx extensions. Alternatively,
you can use third-party extensions such as
`Sphinx AutoAPI <https://sphinx-autoapi.readthedocs.io/en/latest/>`_.

Sphinx has tools for automatically generating API documentation. One
example of this is the ``autodoc`` extension. Here is an example for
how to use it.

.. note::
   
   You will need to write docstrings in reStructuredText format, or see
   the next chapter for how to use the ``napoleon`` extension.

Add the following extensions to ``docs/conf.py``.

.. code-block:: python
    :caption: conf.py

    extensions = [
        "sphinx.ext.autodoc",
    ]

You can get creative here, but I suggest adding your packages,
subpackages, and submodules to an ``api`` directory. Then, for
each package, subpackage, and submodule, create a new RST file.

For example::

    cd docs
    echo "API\n===" > api.rst
    mkdir api; cd api

Then, create a file and directory for ``<your-package>``::

    echo "<your-package>\n============" > <your-package>.rst
    mkdir <your-package>; cd <your-package>

Next, create a file for ``<your-submodule>``::

    echo "<your-package>.<your-submodule>\n=============================" > <your-submodule>.rst

The contents of ``<your-submodule>.rst`` could be something like this,

.. code-block:: rst
    :caption: <your-package>/<your-submodule>.rst

    <your-package>.<your-submodule>
    ===============================

    .. automodule:: <your-package>.<your-submodule>
       :members:

where ``automodule`` automatically parses ``<your-package>.<your-submodule>``
and generates the API documentation from the docstrings. 

Then, we do the same for packages (and subpackages) but follow it with a TOC
for submodules and subpackages.

.. code-block:: rst
    :caption: <your-package>.rst

    <your-package>
    ==============

    .. automodule:: <your-package>
       :members:

    .. toctree::
       :caption: Submodules:

       <your-package>/<your-submodule>

here ``automodule`` parses ``<your-package>/__init__.py`` for docstrings.

Now add a TOC to the file ``docs/api.rst`` to contain all your parent packages
and modules,

.. code-block:: rst
    :caption: api.rst

    API
    ===

    .. toctree::
       :caption: Packages:

       api/<your-package>

Finally, add the API file to your TOC in ``docs/index.rst``,

.. code-block:: rst
    :caption: index.rst

    .. toctree::
       :maxdepth: 2
        
       user-guide
       api

Then, clean and build the documentation,

.. code-block::

   make clean; make html

However, you may see the following warning:

.. code-block::

   WARNING: autodoc: failed to import module '<your-package>'; the following exception was raised:
   No module named '<your-package>'
   WARNING: autodoc: failed to import module '<your-submodule>' from module '<your-package>'; the following exception was raised:
   No module named '<your-package>'

This is because you need to :ref:`install your code locally <locally>` for
``autodoc`` to work. Even if you don't see this warning, you need to
:ref:`tell Readthedocs to install your code <readthedocs>` before compiling the
documentation.
