#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-04-27 16:46:53
# @Last Modified by:   shaolinfm
# @Last Modified time: 2015-06-03 09:38:55

"""
This is simmple script for updating all Python distributives in System
"""

import pip
from subprocess import call

def python_all_packs_update():
    """Function for automatical update of all Python distributives installed in System"""

    for dist in pip.get_installed_distributions():
        call("sudo -H pip install --upgrade " + dist.project_name, shell=True)

if __name__ == '__main__':
    python_all_packs_update()
