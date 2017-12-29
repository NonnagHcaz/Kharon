import unittest
import asyncio
from .context import charon


# def async_test(loop):
#     def handler(f):
#         def wrapper(*args, **kwargs):
#             coro = asyncio.coroutine(f)
#             future = coro(*args, **kwargs)
#             loop.run_until_complete(future)
#         return wrapper
#     return handler

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

    @async_test
    async def test_read_repo(self):
        test_user = 'gannon93'
        test_repo = 'gkit_cogs'
        test_cog = 'vapenaysh'

        res = await charon.get_info(test_user, test_repo, test_cog)
        print(res)
        self.assertTrue(res)
