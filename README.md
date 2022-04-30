## Description

Blog app where user can add, view posts and comment them.

## How to install
* Install python 3
* Create virtualenv
* Git clone this repository
* Use following commands for set-up:

```shell
pip install -r requirements
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

```

## Run Server

```shell
python manage.py runserver
```

## Page urls
- Signup user: http://localhost:8000/user/signup
- Login user: http://localhost:8000/user/login
- Create post: http://localhost:8000/post/create
- View post list: http://localhost:8000/
- View post detail. Add and view comments to post: http://localhost:8000/post/id 



