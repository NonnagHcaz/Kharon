#!/usr/bin/env python3
from __future__ import absolute_import, print_function

try:
    import aiohttp
    import asyncio
    import base64
    ASYNC_FLAG = True
except:
    import requests
    ASYNC_FLAG = False

GITHUB_ENDPOINT = '/'.join(['https://api.github.com', 'repos'])

USER_PATTERN = '/'.join([
    GITHUB_ENDPOINT,
    '{user}'])

REPO_PATTERN = '/'.join([
    GITHUB_ENDPOINT,
    '{user}', '{repo}'])

INFO_PATTERN = '/'.join([
    GITHUB_ENDPOINT,
    '{user}', '{repo}', 'contents', '{cog}', 'info.json'])


class Charon:

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent


def get_info(user, repo, cog):
    url = INFO_PATTERN.format(user=user, repo=repo, cog=cog)

    content = None
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        content = response.json()
    return content


async def get_info_async(user, repo, cog):
    url = INFO_PATTERN.format(user=user, repo=repo, cog=cog)

    content = None
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status is 200:
                data = await response.json()
                content = base64.decodestring(data['content'])
            else:
                print('Content was not found.')
    return content


async def async_test():
    res = await get_info_async('gannon93', 'gkit_cogs', 'vapenaysh')
    print(res)


def sync_test():
    print(get_info('gannon93', 'gkit_cogs', 'vapenaysh'))


if __name__ == '__main__':
    if ASYNC_FLAG:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_test())
        loop.close()
    else:
        sync_test()
