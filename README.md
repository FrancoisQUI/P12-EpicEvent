# P12 Epic Event
12th project from OC DApy Course
"Create an Back end Secured Application with DJANGO ORM"

## Stack

### Requirements :
    - Python 3.x
    - Django 4.02 =<
    - Postgresql
    - venv

### DRF : Django Rest Framework

### [Group and permission management : django-rest-framework-roles](https://github.com/computer-lab/django-rest-framework-roles)

#### Description : 
You have more than one type of user in your data model and you have business logic that diverges depending on the type of user. You do not want to organize your API by role because that is not very RESTful. You do not want to manually type out a lot of conditional branching around user roles.

#### Uses :

### [Settings in .env : django-environ](https://django-environ.readthedocs.io/en/latest/)

#### Description :
django-environ is the Python package that allows you to use Twelve-factor methodology to configure your Django application with environment variables.

#### Uses :
Don't forget to create your own .env file. Copy ```example.env``` and rename it ```.env``` then edit it with your parameters.

### [DRF-extentions](http://chibisov.github.io/drf-extensions/docs/#drf-extensions)

#### Description :
DRF-extensions is a collection of custom extensions for Django REST Framework.

#### Uses :
Used to make [nested routes](http://chibisov.github.io/drf-extensions/docs/#nested-routes)

## Install the site

### Download project and create virtual environnement :

- Download the files or clone the repo where you want 
```shell
cd {your-desired-path}
git git@github.com:FrancoisQUI/P12-EpicEvent.git
cd P12-EpicEvent.git
```
- Create and activate your virtual environnement
```shell
python -m venv {your-desired-env-path*}
source {your-desired-env-path*}/activate
```
*the best choice is 'env'
- Install necessary packages
```shell
pip install -r requirements.txt
```

### Create database :

[create your database in postgresql](https://www.postgresql.org/docs/current/manage-ag-createdb.html)

### Create your .env file :

 - Create a file ```.env``` at the root project
 - Copy paste the content of ```exemple.env``` and enter database information and your secret key

### Create Super-User :

```shell
python manage.py createsuperuser  
```

and follow instructions

### Apply Migrations :

```shell
python manage.py migrate
```

### Apply fixture for right management :

```shell
 python manage.py loaddata auth_group.json
```

### Start server :
- Start the server
```shell
python manage.py runserver 
```

### Give admin rights :
*right management use roles groups, it's important for each account to have one and only one group*

- Acces to the application with your favorite Browser : 
[https://127.0.0.1:8000/admin](https://127.0.0.1:8000/admin)

- Connect the admin

- Add admin group to the admin account

### DEBUG MODE

you can switch between debug mode or production mode in ```epic_event/settings.py``` :
set ```DEBUG``` to ```True``` or ```Flase```
