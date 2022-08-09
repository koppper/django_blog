Clone repository

git clone https://github.com/koppper/django_blog.git


Create virtual environment

virtualenv myvenv


Activate virtual environment

source myvenv/bin/activate/


Install dependencies

pip3 install -r requirements.txt


Migrate database

python3 manage.py migrate


Run server

python3 manage.py runserver



http://127.0.0.1:8000 - home page 
http://127.0.0.1:8000/1  -  check the detail post with id
http://127.0.0.1:8000/create_post/  -  create new post 
