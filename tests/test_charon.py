import unittest
import asyncio
from .context import kharon
import json
import os

HERE = os.path.abspath(os.path.dirname(__file__))

TEST_USER = 'gannon93'
TEST_REPO = 'gkit_cogs'
TEST_COG = 'vapenaysh'

TEST_DATA = json.load(open(os.path.join(HERE, 'data', 'info.json')))


def async_test(loop):
    def handler(f):
        def wrapper(*args, **kwargs):
            coro = asyncio.coroutine(f)
            future = coro(*args, **kwargs)
            loop.run_until_complete(future)
        return wrapper
    return handler


class kharonTests(unittest.TestCase):
    def setUp(self):
        self.kharon = kharon.kharon()

    def tearDown(self):
        pass

    def test_format_info(self):
        data = kharon.format_info(
            TEST_DATA)

        self.assertTrue(_format_info_helper(data))

    def test_get_and_format_info(self):

        data = kharon.get_and_format_info(
            TEST_USER, TEST_REPO, TEST_COG)

        self.assertTrue(_format_info_helper(data))

    @async_test(asyncio.new_event_loop())
    async def test_get_and_format_info_async(self):

        data = await kharon.get_and_format_info_async(
            TEST_USER, TEST_REPO, TEST_COG)

        self.assertTrue(_format_info_helper(data))

    def test_get_info(self):

        data = kharon.get_info(
            TEST_USER, TEST_REPO, TEST_COG)

        self.assertTrue(_get_info_helper(data))

    @async_test(asyncio.new_event_loop())
    async def test_get_info_async(self):

        data = await kharon.get_info_async(
            TEST_USER, TEST_REPO, TEST_COG)

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
