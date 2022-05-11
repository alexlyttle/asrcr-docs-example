Adding code
===========

.. note::
    
    If you are creating stand-alone documentation, you can skip this chapter.

So you have some basic documentation, but no code to go with it!

Example
-------

Let's create a Python package called ``wordie``. In the base directory
of your project,

.. code-block::

    mkdir wordie

Now let's create some files in the ``wordie`` directory. How about
a module containing a class called ``Letters`` which has a method
for randomly shuffling some letters. We first initialise the package,

.. code-block:: python
    :caption: __init__.py

    from .letters import Letters

Then, we create the letters module,

.. code-block:: python
    :caption: letters.py

    import random


    class Letters:
        """Class for letters."""
        def __init__(self, s: str):
            if not s.isalpha():
                raise ValueError("String must be only letters.")
            self._s = s
        
        def __repr__(self):
            return f"Letters({self._s})"

        def __str__(self):
            return self._s

        def shuffle(self):
            """Shuffle the letters"""
            self._s = ''.join(random.sample(self._s, len(self._s)))

We can test this code by running this script in the project directory,

.. code-block:: python

    from wordie import Letters

    l = Letters("abcdef")
    print(l)
    l.shuffle()
    print(l)

which should print the original letters followed by the shuffled letters.

Install
-------

Locally
^^^^^^^

Your code should be installed in your environment to generate the docs.
If you haven't already, install it by going to the project directory
and running,

.. code-block::

    pip install .

You will need to add a few more files to ``.gitignore``,

.. code-block::
    :caption: .gitignore
    
    __pycache__/
    *.egg-info

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
