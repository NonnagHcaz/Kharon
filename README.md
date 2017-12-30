[![Travis - Linux](https://img.shields.io/travis/gannon93/charon.svg?label=Linux%20Status)](https://travis-ci.org/gannon93/charon) [![AppVeyor - Windows](https://img.shields.io/appveyor/ci/Gannon93/charon.svg?label=Windows%20Status)](https://ci.appveyor.com/project/Gannon93/charon)  
[![Codecov](https://img.shields.io/codecov/c/github/gannon93/charon.svg?label=Coverage)](https://codecov.io/github/gannon93/charon?branch=master) [![Code Health](https://landscape.io/github/gannon93/charon/master/landscape.svg?style=flat&label=Health)](https://landscape.io/github/gannon93/charon/master)  

# Charon
The ferryman you need to travel the gap from Red v2 to Red v3.

---

## DESCRIPTION

Charon is a python module that will assist you in transitioning your Red-discordBot cogs from v2 to v3.

Notably, Charon will:

- Format `info.json` files
- Add `__init__.py` files with standard setup details
- Convert old `util` and `data.IO` imports to new imports

---

## INSTALL

_**Not yet on PyPI**_, but when it is:

> python -m pip install charon

---

## USAGE

Charon can be imported to be used in custom scripts and modules, ran from the command line as a service, or tested at the live site.

### Option 1: Module Import

```python
import charon  
data = await charon.format_info_async(  
    user='github_user', repo='repo_name', cogs='cog_name')
print(data)
```

If no cogs are listed, then Charon will run for all cogs in the repository.

### Option 2: CLI Command

> $ charon -u <github_user> -r <repo_name> -c <cog_name> (optional)

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
