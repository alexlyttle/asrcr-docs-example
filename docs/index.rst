.. asr-docs-example documentation master file, created by
   sphinx-quickstart on Wed May 11 12:15:41 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ASR Code Review - Documentation
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   publish
   adding-code
   api-generation
   better-docstrings
   extras
   api


Getting started
===============

So you want to build some documentation for your project. Follow this
guide to get started.

Setup project
-------------

.. note::
   
   If you are already working on a project, you may start at 
   step 3 after navigating to your project directory.

1. Create an empty repository (e.g. using GitHub, GitLab, or Bitbucket)

2. Clone the repository onto your local machine

3. Create and move to the documentation directory,

   .. code-block::

      mkdir docs
      cd docs

4. Add ``sphinx`` to a requirements file and install it,
   
   .. code-block::

      echo sphinx >> requirements.txt
      pip install sphinx

5. Run quickstart to setup the documentation,
   
   .. code-block::
      
      sphinx-quickstart

6. Build and preview the documentation locally,
   
   .. code-block::

      make html
      open _build/html/index.html

7. Add build directory to gitignore
   
   .. code-block::

      echo _build >> .gitignore

8. Commit the documentation to the repository,
   
   .. code-block::

      cd ../
      git add .
      git commit -m "Initial documentation"
      git push

You now have a working Sphinx project!

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

Adding a new page
-----------------

Let's add a new page to our documentation.

.. code-block::

   cd docs
   echo "Publishing documentation\n========================" > publish.rst

Now, add the new page to the table of contents at the top of ``index.rst``.

.. code-block:: rst
   
   .. toctree::
      :maxdepth: 2
      :caption: Contents:
      
      publish  .. <-- add pages here

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
