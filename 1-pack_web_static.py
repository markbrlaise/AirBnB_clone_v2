#!/usr/bin/env python3
# fabfile to generate a .tgz compressed file from web_static
from fabric.api import local
from datetime import datetime
import time


def do_pack():
    """
    compress web_static/ and store compressed file at versions/web_static<year>
    <month><day><hour><minute><second>.tgz
    """
    clocktime = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")

    try:
        local('mkdir -p versions/')
        local_tar = local(
            'tar -czvf versions/web_static_{}.tgz web_static/'
            .format(clocktime))
        return local_tar
    except Exception:
        return None
