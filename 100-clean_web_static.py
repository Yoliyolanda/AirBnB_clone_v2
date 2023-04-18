#!/usr/bin/python3
"""This script deletes out-of-date archives, using the function do_clean"""
from fabric.api import *


env.hosts = ['34.224.2.192', '100.25.3.122']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
