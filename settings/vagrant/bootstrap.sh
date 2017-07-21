#!/bin/sh -e
sudo apt-get -y update
sudo apt-get -y install postgresql-server-dev-9.1 postgresql-9.1 postgresql-contrib-9.1
sudo apt-get -y install  nginx memcached python-pip libjpeg-dev libffi-dev
sudo apt-get -y install  python-dev g++ vim supervisor build-essential coffeescript fabric
sudo pip install gunicorn psycopg2 python-memcached pytest-django pytest-xdist
sudo pip install -r /vagrant/requirements.txt
sudo pip install django-debug-toolbar django-statsd-mozilla https://github.com/graphite-project/ceres/tarball/master whisper carbon graphite-web
sudo rm -rf /usr/local/lib/python2.7/dist-packages/django
sudo rm -rf /usr/local/lib/python2.7/dist-packages/Django-1.11.2-py2.7.egg-info
sudo pip install -r /vagrant/requirements.txt
