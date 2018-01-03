|Travis - Linux| |AppVeyor - Windows| |Codecov| |Code Health|

Charon
======

The ferryman you need to travel the gap from Red v2 to Red v3.

--------------

DESCRIPTION
-----------

Charon is a python module that will assist you in transitioning your
Red-discordBot cogs from v2 to v3.

Notably, Charon will:

-  Format ``info.json`` files
-  Add ``__init__.py`` files with standard setup details
-  Convert old ``util`` and ``data.IO`` imports to new imports

Charon also provides both synchronous and asynchronous versions of any
method performing HTTP requests.

--------------

INSTALL
-------

***Not yet on PyPI***, but when it is:

    python -m pip install Charon

--------------

REQUIREMENTS
------------

You need at least one of the following:

-  ``requests`` for synchronous requests
-  ``aiohttp`` for asynchronous requests

When installing ``Charon`` with pip, both ``requests`` and ``aiohttp``
will be downloaded as well as ``Charon``.

--------------

USAGE
-----

Charon can be imported to be used in custom scripts and modules, ran
from the command line as a service, or tested at the live site.

Option 1: Module Import
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from charon import charon

    data = charon.format_info(
        user='github_user', repo='repo_name', cogs='cog_name')
    print(data)

If no cogs are listed, then Charon will run for all cogs in the
repository.

Option 2: CLI Command
~~~~~~~~~~~~~~~~~~~~~

    $ Charon -u <github_user> -r <repo_name> -c <cog_name> (optional)

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
.. _Demo: https://gannon93.pythonanywhere.com/charon
.. _@Redjumpman: https://github.com/Redjumpman
.. _MIT: https://github.com/gannon93/gkit_cogs/blob/master/LICENSE

.. |Travis - Linux| image:: https://img.shields.io/travis/gannon93/Charon.svg?label=Linux%20Status
   :target: https://travis-ci.org/gannon93/Charon
.. |AppVeyor - Windows| image:: https://img.shields.io/appveyor/ci/Gannon93/Charon.svg?label=Windows%20Status
   :target: https://ci.appveyor.com/project/Gannon93/Charon
.. |Codecov| image:: https://img.shields.io/codecov/c/github/gannon93/Charon.svg?label=Coverage
   :target: https://codecov.io/github/gannon93/Charon?branch=master
.. |Code Health| image:: https://landscape.io/github/gannon93/Charon/master/landscape.svg?style=flat&label=Health
   :target: https://landscape.io/github/gannon93/Charon/master
