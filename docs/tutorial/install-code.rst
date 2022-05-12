Install your code
=================

.. _locally:

Locally
-------

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
-----------

Readthedocs also needs to install your code for extensions such as ``autodoc``
to work. Create a file named ``.readthedocs.yaml`` in the root of your project.
This example configures the documentation to build on Ubuntu with Python 3.9 and
for python to install our package along with requirements for building the
documentation.

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

Publish your code
-----------------

You could use `flit <https://flit.pypa.io/en/latest/>`_ to publish your code
on PyPI. That way, others can simple install is like so::

   pip install <your-package>

This also allows you to install the package locally in editable mode using::

   pip install -e .
