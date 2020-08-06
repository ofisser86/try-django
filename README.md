[![Try Django 2.2 tutorial](try_django_2_2_share.jpg)]
### Getting Started

#### Requirements
- Python 3.6 & up
- Virtual Environment (pipenv or virtualenv)


#### 1. Create Virtual Environment & Install Django
```
cd /path/to/dev/folder
mkdir try_django
cd try_django
pipenv --python 3.6 install django==2.2
pipenv shell
```
> Don't have pipenv? Check out [doc](https://pipenv-fork.readthedocs.io/en/latest/)

#### 2. Create Django Project
```
cd /path/to/dev/folder
mkdir src
cd src
django-admin startproject try_django .
```

#### 3. Setup Project in Visual Studio Code
This is optional. Download it on https://code.visualstudio.com/
