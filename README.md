[![Travis - Linux](https://img.shields.io/travis/gannon93/Kharon.svg?label=Linux%20Status)](https://travis-ci.org/gannon93/Kharon) [![AppVeyor - Windows](https://img.shields.io/appveyor/ci/Gannon93/Kharon.svg?label=Windows%20Status)](https://ci.appveyor.com/project/Gannon93/Kharon) [![Codecov](https://img.shields.io/codecov/c/github/gannon93/Kharon.svg?label=Coverage)](https://codecov.io/github/gannon93/Kharon?branch=master) [![Code Health](https://landscape.io/github/gannon93/Kharon/master/landscape.svg?style=flat&label=Health)](https://landscape.io/github/gannon93/Kharon/master)  

# Kharon
The ferryman you need to travel the gap from Red v2 to Red v3.

_**Join my Discord server: https://discord.gg/zw7NmT**_

---

## DESCRIPTION

Kharon is a python module that will assist you in transitioning your Red-discordBot cogs from v2 to v3.

Notably, Kharon will:

- Format `info.json` files

Kharon also provides both synchronous and asynchronous versions of any method performing HTTP requests.

---

## INSTALL

_**Now on PyPI!**_

> python -m pip install Kharon

---

## REQUIREMENTS

You need at least one of the following:

- `requests` for synchronous requests
- `aiohttp` for asynchronous requests

When installing with pip, both `requests` and `aiohttp` will be downloaded as well as `Kharon`.

---

## USAGE

Kharon can be imported to be used in custom scripts and modules, ran from the command line as a service, or tested at the live site.

### Option 1: Module Import

```python
from kharon import kharon  

data = kharon.format_info(  
    user='github_user', repo='repo_name', cogs='cog_name')  
print(data)  

```

If no cogs are listed, then Kharon will run for all cogs in the repository.

### Option 2: CLI Command

> $ Kharon -u <github_user> -r <repo_name> -c <cog_name> (optional)


### Option 3: Live Demo

Visit my [personal webpage](https://gannon93.pythonanywhere.com/), built with Django and hosted by the wonderful people at PythonAnywhere, or go directly to the [Demo](https://gannon93.pythonanywhere.com/Kharon).

---

## CONTRIBUTION

Follow these 5 easy steps for a successful contribution (by [@Redjumpman](https://github.com/Redjumpman)):

  1. Fork it!
  2. Develop your feature branch
  3. Commit your changes
  4. Push to the main branch
  5. Submit a pull request

---

## LICENSE

The project is licensed under [MIT](https://github.com/gannon93/gkit_cogs/blob/master/LICENSE). Feel free to alter this project anyway you see fit, as long as I am credited for the original work.
