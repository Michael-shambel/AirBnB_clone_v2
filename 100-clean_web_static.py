#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""
from fabric.api import *
from os.path import exists

env.hosts = ['54.174.253.226', '35.168.1.245']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    try:
        number = int(number)
    except ValueError:
        return

    number = 1 if number == 0 else number

    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs -I {{}} rm {{}}'.format(number + 1))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}'.format(number + 1))
