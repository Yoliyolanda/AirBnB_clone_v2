#!/usr/bin/python3
"""This script that distributes an archive to your web servers"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['100.25.180.155', '100.26.173.28']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school' 

def do_deploy(archive_path):
    """ Deploys files to server"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_filename = os.path.basename(archive_path)
        archive_folder = "/data/web_static/releases/{}".format(
            archive_filename.split(".")[0])
        run("mkdir -p {}".format(archive_folder))
        run("tar -xzf /tmp/{} -C {}".
            format(archive_filename, archive_folder))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {}/web_static/* {}/".format(archive_folder, archive_folder))
        run("rm -rf {}/web_static".format(archive_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(archive_folder))
        return True
    except:
        return False
