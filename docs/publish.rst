Publishing documentation
========================

You can publish the documentation to a `GitHub Pages <https://pages.github.com/>`_,
but this tutorial will show you how to use `Read the Docs <https://readthedocs.org/>`_.

Readthedocs
-----------

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
