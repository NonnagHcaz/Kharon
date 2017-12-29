#!/usr/bin/env python3
from __future__ import absolute_import, print_function

import base64
import requests
import os

GITHUB_ENDPOINT = 'https://api.github.com/repos'

USER_PATTERN = os.path.join(
    GITHUB_ENDPOINT,
    '{user}')

REPO_PATTERN = os.path.join(
    GITHUB_ENDPOINT,
    '{user}/{repo}')

INFO_PATTERN = os.path.join(
    GITHUB_ENDPOINT,
    '{user}/{repo}/contents/blob/{branch}/{cog}/info.json')


class Charon:

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent


def get_info(user, repo, cog, branch='master'):
    url = INFO_PATTERN.format(user=user, repo=repo, cog=cog, branch=branch)
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()  # the response is a JSON
        # req is now a dict with keys: name, encoding, url, size ...
        # and content. But it is encoded with base64.
        content = base64.decodestring(req['content'])
    else:
        print('Content was not found.')

