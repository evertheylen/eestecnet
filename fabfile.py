from fabric.operations import local

__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def remove_migrations():
    apps = local('ls -1 apps', capture=True).split()
    for app in apps:
        try:
            local('rm apps/' + app + '/migrations/0*')
        except:
            pass
    try:
        local('rm common/migrations/0*')
    except:
        pass


