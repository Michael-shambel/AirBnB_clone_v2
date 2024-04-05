#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using
the function do_deploy
"""
from fabric.api import *
from os.path import exists


env.hosts = ['100.25.34.19', '100.27.2.0']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False

    name = archive_path.split('/')[-1]
    no_ext = name.split('.')[0]

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            name, no_ext))
        run('rm /tmp/{}'.format(name))
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(no_ext, no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ '
            '/data/web_static/current'.format(no_ext))
        return True
    except Exception as e:
        return False
