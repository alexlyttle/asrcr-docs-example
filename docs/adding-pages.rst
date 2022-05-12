Adding pages
============

Let's add a new page to our documentation.

.. code-block::

   cd docs
   echo "Adding pages\n=============" > adding-pages.rst

Now, add the new page to the table of contents at the top of ``index.rst``.

.. code-block:: rst
   
   .. toctree::
      :maxdepth: 2
      :caption: Contents:
      
      adding-pages  .. <-- add pages here

Documentation is generated from reStructuredText files (``.rst`` or ``.rest``).
For a primer on reStructuredText, see
`here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.
Below, we will cover a few basics.

.. note::

    If you prefer to use markdown over reStructuredText, you can use the
    `MyST <https://myst-parser.readthedocs.io/en/latest/using/intro.html>`_ 
    extension. If so, you may skip the rest of this chapter.

Headings
--------

There are several ways to create headings in reStructuredText, but simply
you may underline the headings like so,

* ``=`` for sections
* ``-`` for subsections
* ``^`` for subsubsections
* ``"`` for paragraphs

Lists
-----

Code blocks
-----------

