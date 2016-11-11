Paquetes necesarios: 

* python-dev
* postgresql
* postgresql-server-dev-all
* python-virtualenv
* virtualenvwrapper

Clone the repository: 

    $ git clone 

Create and activate the virtual environment

    $ mkvirtualenv -p /usr/bin/python3.5 snippets
    $ workon snippets

Install the requirements: 

    (snippets)$ pip install -r requirements.txt

To install django-bootstrap3-datetimepicker without errors you have to do it from the main branch and not from the one in the official releases: 

    (snippets)$ pip install git+https://github.com/nkunihiko/django-bootstrap3-datetimepicker.git

Create the database and the database user: 

    $ sudo -u postgres psql
    postgres=# CREATE ROLE snippets LOGIN PASSWORD 'snippets-123qwe' NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
    postgres=# CREATE DATABASE snippets WITH OWNER = snippets;


You have to create your own local_config.py with your local database credentials: 


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'snippets',
            'USER':'snippets',
            'PASSWORD':'snippets-123qwe',
        }
    }

Then you have to import this new file in settings.py: 

    from .local_config import *

and delete the definition of DATABASES in settings.py because you are importing it from local_config.py

Initialize the database and set-up the Django environment: 

    (snippets)$ cd snippets/
    (snippets)$ ./manage.py bower_install
    (snippets)$ ./manage.py collectstatic
    (snippets)$ ./manage.py makemigrations
