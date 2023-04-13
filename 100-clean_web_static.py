#!/usr/bin/python3
# fabfile to delete out of date files

import os
from fabric.api import env
from fabric.operations import local, cd, lcd, run


def do_clean(number=0):
    # get number variable playing a big role

    number = 1 if int(number) == 0 else int(number)

    # delete in local env (versions/)
    archives = sorted(os.listdir("versions"))
    outdated = [archives.pop() for i in range(number)]
    with lcd("versions/"):
        for arch in outdated:
            local("rm -rf {}".format(arch))

    # delete remote envs
    with cd("/data/web_static/releases/"):
        all_archives = run("ls -t").split()
        archives = [a for a in all_archives if "web_static" in a]
        outdated = [archives.pop() for i in range(number)]
        for arch in outdated:
            run("rm -rf {}".format(arch))

