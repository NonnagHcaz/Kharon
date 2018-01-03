
Kharon
======

The ferryman you need to travel the gap from Red v2 to Red v3.

--------------

DESCRIPTION
-----------

Kharon is a python module that will assist you in transitioning your
Red-discordBot cogs from v2 to v3.

Notably, Kharon will:

-  Format ``info.json`` files
-  Add ``__init__.py`` files with standard setup details
-  Convert old ``util`` and ``data.IO`` imports to new imports

Kharon also provides both synchronous and asynchronous versions of any
method performing HTTP requests.

--------------

INSTALL
-------

***Not yet on PyPI***, but when it is:

    python -m pip install Kharon

--------------

REQUIREMENTS
------------

You need at least one of the following:

-  ``requests`` for synchronous requests
-  ``aiohttp`` for asynchronous requests

When installing ``Kharon`` with pip, both ``requests`` and ``aiohttp``
will be downloaded as well as ``Kharon``.

--------------

USAGE
-----

kharon can be imported to be used in custom scripts and modules, ran
from the command line as a service, or tested at the live site.

Option 1: Module Import
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from kharon import kharon

    data = kharon.format_info(
        user='github_user', repo='repo_name', cogs='cog_name')
    print(data)

If no cogs are listed, then Kharon will run for all cogs in the
repository.

Option 2: CLI Command
~~~~~~~~~~~~~~~~~~~~~

    $ kharon -u <github_user> -r <repo_name> -c <cog_name> (optional)

Option 3: Live Demo
~~~~~~~~~~~~~~~~~~~

Visit my `personal webpage`_, built with Django and hosted by the
wonderful people at PythonAnywhere, or go directly to the `Demo`_.

--------------

CONTRIBUTION
------------

Follow these 5 easy steps for a successful contribution (by
`@Redjumpman`_):

1. Fork it!
2. Develop your feature branch
3. Commit your changes
4. Push to the main branch
5. Submit a pull request

--------------

LICENSE
-------

The project is licensed under `MIT`_. Feel free to alter this project
anyway you see fit, as long as I am credited for the original work.

.. _personal webpage: https://gannon93.pythonanywhere.com/
.. _Demo: https://gannon93.pythonanywhere.com/kharon
.. _@Redjumpman: https://github.com/Redjumpman
.. _MIT: https://github.com/gannon93/gkit_cogs/blob/master/LICENSE

