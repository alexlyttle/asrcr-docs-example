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

.. note::
   
   You will need to write docstrings in reStructuredText format, or see
   the next chapter for how to use the ``napoleon`` extension.

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

    .. automodule:: <your-package>
       :members:

    .. toctree::
       :caption: Submodules:

       <your-package>.<your-submodule>

Here, we create a TOC for any submodules in the package (you may
create a separate TOC for subpackages etc.) and and precede it with
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

Install your code
-----------------

.. _locally:

Locally
^^^^^^^

Your code should be installed in your environment to generate the docs.
If you haven't already, install it by going to the project directory
and running,

.. code-block::

    pip install .

You will also need to add a few more files to ``.gitignore``,

.. code-block::
    :caption: .gitignore
    
    __pycache__/
    *.egg-info

.. _readthedocs:

Readthedocs
^^^^^^^^^^^

Readthedocs also needs to know to install your code. Create a file
named ``.readthedocs.yaml`` in the root of your project. This example
configures the documentation to build on Ubuntu with Python 3.9 and
for python to install our package.

.. code-block:: yaml
    :caption: .readthedocs.yaml

    version: 2

    build:
      os: "ubuntu-20.04"
      tools:
        python: "3.9"

    python:
    # Install our python package before building the docs
      install:
        - method: pip
          path: .
        - requirements: docs/requirements.txt
