.. asr-docs-example documentation master file, created by
   sphinx-quickstart on Wed May 11 12:15:41 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to my example documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Getting started
---------------

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

Configuration
-------------

Sphinx features several options and extensions that can be configured.

Theme
^^^^^

Sphinx comes with `builtin themes <https://www.sphinx-doc.org/en/master/usage/theming.html>`_.
This documentation uses the `Sphinx Book Theme <https://sphinx-book-theme.readthedocs.io/en/stable/>`_

1. Add the theme to the requirements and install it,

   .. code-block::

      echo sphinx-book-theme >> docs/requirements.txt
      pip install sphinx-book-theme

2. Go to the ``conf.py`` file and add the following lines,

   .. code-block::

      html_theme = 'sphinx_book_theme'

This theme allows you to add hyperlinks to the source repository and more.

Publish
-------

You can publish the documentation to a `GitHub Pages <https://pages.github.com/>`_,
but this tutorial will show you how to use `Read the Docs <https://readthedocs.org/>`_.

Ensure that your project has a ``docs/requirements.txt`` file with all
Python packages needed to build the documentation. Optionally, add
`configuration options <https://docs.readthedocs.io/en/stable/config-file/index.html>`_ 
to the file ``.readthedocs.yaml``.

1. Go to `readthedocs.org <https://readthedocs.org/>`_ and sign in or make an acount

2. Go to your `Dashboard <https://readthedocs.org/dashboard/>`_ and Import a Project

3. To `Import Manually <https://docs.readthedocs.io/en/stable/intro/import-guide.html#manually-import-your-docs>`_,
   enter your project details into the form

Or,

3. Go to `Connected Services <https://readthedocs.org/accounts/social/connections/>`_ and connect your
   GitHub, GitLab, or Bitbucket account

4. Find your repository and click the plus icon

You should now be able to view your documentation live on the internet!
It will update every time you push to the specified branch, so ensure
that your documentation compiles correctly before publishing.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
