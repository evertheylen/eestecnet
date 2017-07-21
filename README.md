# eestec.net

*eestec.net* is an open source project destined to provide an online platform for the
Electrical Engineering Students' European Association (EESTEC). Its purpose is to serve
as a central communication and administration hub for the association and to preserve knowledge for
future generations.

## How to set it up

### Local Environment
Everything will run inside a virtual machine on your machine, with all dependencies and tools encapsulated in that machine. We use Vagrant to manage the virtual machine. Depending on your machine the following steps to pull the project and set up for local development may take several minutes.

#### Debian/Ubuntu
```sudo apt-get install git virtualbox vagrant
vagrant plugin install vagrant-reload
git clone https://github.com/eestecitt/eestecnet.git
vagrant up
```
When it finishes, you should check localhost:8005 for a running instance of eestecnet.

If you encounter any problems then try this sequence of commands:
```
vagrant ssh
cd /vagrant/
sudo service supervisor stop
sudo killall python
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```
