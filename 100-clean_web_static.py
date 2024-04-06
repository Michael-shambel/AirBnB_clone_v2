#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives,
using the function do_clean
"""
from fabric.api import *
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    try:
        number = int(number)
    except ValueError:
        print("Invalid number provided.")
        return

    if number < 0:
        print("Number must be a non-negative integer.")
        return

    # Delete unnecessary archives in versions folder
    local("ls -t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}"
          .format(number + 1))

    for host in env.hosts:
        with settings(host_string=host):
            releases = run("ls -t /data/web_static/releases/")
            releases_list = releases.split()
            if len(releases_list) > number:
                to_delete = releases_list[number:]
                for archive in to_delete:
                    run("rm -rf /data/web_static/releases/{}".format(archive))
