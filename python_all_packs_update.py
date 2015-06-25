#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-04-27 16:46:53
# @Last Modified by:   shaolinfm
# @Last Modified time: 2015-06-25 17:04:21

"""
This is simmple script for updating all Python distributives in System
"""

import pip
from subprocess import call

def python_all_packs_update():
    """Function for automatical update of all Python distributives installed in System"""
    try:
        for dist in pip.get_installed_distributions():
            call("sudo pip install -U pip", shell=True)
            call("sudo -H pip install --upgrade " + dist.project_name, shell=True)

    except Exception as e:
        print "Unexpected error:", type(e), e

if __name__ == '__main__':
    python_all_packs_update()
