import unittest
import asyncio
from .context import charon

TEST_USER = 'gannon93'
TEST_REPO = 'gkit_cogs'
TEST_COG = 'vapenaysh'


def async_test(loop):
    def handler(f):
        def wrapper(*args, **kwargs):
            coro = asyncio.coroutine(f)
            future = coro(*args, **kwargs)
            loop.run_until_complete(future)
        return wrapper
    return handler


class CharonTests(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.charon = charon.Charon()

    def tearDown(self):
        pass

    def test_format_info(self):

        data = charon.format_info(TEST_USER, TEST_REPO, TEST_COG)

        self.assertTrue(_format_info_helper(data))

    @async_test(asyncio.new_event_loop())
    async def test_format_info_async(self):

        data = await charon.format_info_async(TEST_USER, TEST_REPO, TEST_COG)

        self.assertTrue(_format_info_helper(data))

    def test_get_info(self):

        data = charon.get_info(TEST_USER, TEST_REPO, TEST_COG)

        self.assertTrue(_get_info_helper(data))

    @async_test(asyncio.new_event_loop())
    async def test_get_info_async(self):

        data = await charon.get_info_async(TEST_USER, TEST_REPO, TEST_COG)

        self.assertTrue(_get_info_helper(data))


def _get_info_helper(data):
    repo_author = True if data['AUTHOR'] in 'Gannon' else False
    repo_name = True if data['NAME'] in 'VapeNaysh' else False
    return(repo_name and repo_author)


def _format_info_helper(data):
    repo_author = True if data['author'][0] in 'Gannon' else False
    repo_hidden = True if 'hidden' in data.keys() else False
    repo_disabled = True if 'DISABLED' not in data.keys() else False
    return(repo_hidden and repo_disabled and repo_author)
