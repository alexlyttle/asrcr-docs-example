Adding pages
============

Let's add a new section to our documentation to contain the user guide.

.. code-block::

   cd docs
   echo "User guide\n==========" > user-guide.rst

Now, add the new page to the table of contents at the top of ``index.rst``.

.. code-block:: rst
   :caption: index.rst
   
   .. toctree::
      :maxdepth: 2
      
      user-guide

In ``user-guide.rst`` we can add a TOC tree to other pages in the documentation
relating to the user guide. For example, let's create a page for installation
instructions and a page for release notes contained in a new directory.

.. code-block::

   mkdir user-guide; cd user-guide
   echo "Installation\n============" > installation.rst
   echo "Release notes\n=============" > release-notes.rst

We then add the new pages to the table of contents at the top of
``user-guide.rst``.

.. code-block::
   :caption: user-guide.rst

   .. toctree::
      :maxdepth: 2
      
      user-guide/installation.rst
      user-guide/release-notes.rst

You may then go into ``installation.rst`` and ``release-notes.rst`` and write
the documentation.

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

Example
-------

For this documentation, ``user-guide.rst`` looks like this:

.. code-block:: rst
   :caption: user-guide.rst

   User guide
   ==========

   This is an example user guide to the ASR Code Review documentation tutorial.
   You can emphasises text like *this* and embolden text like **this**. Inline
   code can be written like ``this`` and hyperlinks can be written like
   `this <https://www.youtube.com/watch?v=dQw4w9WgXcQ>`_.

   .. toctree::
      :maxdepth: 2
      
      user-guide/installation.rst
      user-guide/release-notes.rst
