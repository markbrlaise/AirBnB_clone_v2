#!/usr/bin/env python3
# create archive and do deploy to servers


from fabric.api import env
from fabric.operations import local, sudo


env.hosts = ['34.232.69.85', '52.87.154.146']

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

def deploy():
    # if do_pack is false: return false
    archive_path = do_pack()
    if archive_path is None:
        return False
    do_deploy(archive_path)
    # otherwise: do_deploy(do_pack)

"""

in an alternate universe... simplicity 
def deploy():
    try:
        # call do_pack and keep path
        archive_path = local("fab -f 1-pack_web_static.py do_pack")
        # call do_deploy and return value of do_deploy
        deploy = local("
                fab -f 2-do_deploy_web_static.py do_deploy:
                {} -i ../.rsa/keys -u ubuntu".format(archive_pth))
    except FileNotFoundError:
        return False
        
"""

