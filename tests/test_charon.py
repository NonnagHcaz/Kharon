import unittest
import asyncio
from .context import charon


def async_test_thread(loop):
    def handler(f):
        def wrapper(*args, **kwargs):
            coro = asyncio.coroutine(f)
            future = coro(*args, **kwargs)
            loop.run_until_complete(future)
        return wrapper
    return handler


def async_test(f):
    def wrapper(*args, **kwargs):
        coro = asyncio.coroutine(f)
        future = coro(*args, **kwargs)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)
        loop.close()
    return wrapper


class CharonTests(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        pass

    @async_test_thread(asyncio.new_event_loop())
    async def test_format_info_async(self):
        test_user = 'gannon93'
        test_repo = 'gkit_cogs'
        test_cog = 'vapenaysh'

        res = await charon.format_info_async(test_user, test_repo, test_cog)
        repo_author = True if res['author'] in 'Gannon' else False
        repo_hidden = True if 'hidden' in res.keys() else False
        repo_disabled = True if 'DISABLED' not in res.keys() else False

        self.assertTrue(repo_hidden and repo_disabled and repo_author)

    def test_get_info(self):
        test_user = 'gannon93'
        test_repo = 'gkit_cogs'
        test_cog = 'vapenaysh'

        res = charon.get_info(test_user, test_repo, test_cog)
        repo_author = True if res['AUTHOR'] in 'Gannon' else False
        repo_name = True if res['NAME'] in 'VapeNaysh' else False

        self.assertTrue(repo_name and repo_author)

    @async_test_thread(asyncio.new_event_loop())
    async def test_get_info_async(self):
        test_user = 'gannon93'
        test_repo = 'gkit_cogs'
        test_cog = 'vapenaysh'

        res = await charon.get_info_async(test_user, test_repo, test_cog)
        repo_author = True if res['AUTHOR'] in 'Gannon' else False
        repo_name = True if res['NAME'] in 'VapeNaysh' else False

        self.assertTrue(repo_name and repo_author)
