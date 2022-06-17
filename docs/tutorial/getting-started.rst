Getting started
===============

So you want to build some documentation for your project. Follow this
guide to get started.

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
   
   .. tab:: macOS

      .. code-block:: bash

         make html
         open _build/html/index.html

   .. tab:: Linux

      .. code-block:: bash

         make html
         xdg-open _build/html/index.html

7. Add build directory to gitignore (optional)
   
   .. code-block::

      echo _build >> .gitignore

8. Commit the documentation to the repository,
   
   .. code-block::

      cd ../
      git add .
      git commit -m "Initial documentation"
      git push

You now have a working Sphinx project!