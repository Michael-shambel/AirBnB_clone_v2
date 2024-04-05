#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive
 from the contents of the web_static folder
 of your AirBnB Clone repo, using the function do_pack."""
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    All files in the folder web_static must be added to the final archive
    """
    local("mkdir -p versions")
    time = datetime.now()
    archive = "web_static_{}.gtz".format(time.strftime("%Y%m%d%H%M%S"))
    result = local("tar -czvf versions/{} web_static".format(archive))
    if result is None:
        return None
    else:
        return archive
