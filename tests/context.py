# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from charon import charon

BASEDIR = './tests'
DATA_DIR = os.path.join(BASEDIR, 'data')
