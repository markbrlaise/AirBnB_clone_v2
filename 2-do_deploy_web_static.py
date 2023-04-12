#!/usr/bin/env python3
"""deploying web_static"""


from fabric.operations import sudo, put
from fabric.api import env

env.hosts = ['34.232.69.85', '52.87.154.146']


def do_deploy(archive_path):
    try:
        put(archive_path, "/tmp/")
        archive_file = archive_path.split("/")[-1]
        folder_file = "/data/web_static/releases/" + archive_file.split(".")[0]
        sudo("mkdir -p {}".format(folder_file))
        sudo("tar -xzf /tmp/{} -C {}".format(archive_file, folder_file))
        sudo("mv {}/web_static/* {}/".format(folder_file, folder_file))
        sudo("rm -rf {}/web_static".format(folder_file))
        sudo("rm -rf /tmp/{}".format(archive_file))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -sf {} /data/web_static/current".format(folder_file))
        print("New Version deployed")
        return True
    except Exception:
        return False
