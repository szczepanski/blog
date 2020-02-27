```

# python pre-reqs 
pip3.8 install Django
pip3.8 install pillow


# create blank new repo on github
szczepanski/blog



django-admin startproject blog_core
mv blog_core blog
cd blog
git init
git remote add origin https://github.com/szczepanski/blog.git
git add -A
it commit -m 'updated readme'
git push -u origin master

# init first two apps 
python3.8 manage.py startapp app_blog
python3.8 manage.py startapp app_projects

# add new apps to blog_core/settings.py --> INSTALLED_APPS
'app_blog',
'app_projects',

# check the server
python3.8 manage.py runserver

# migrations - db model changes

# discover new migrations / db model changes (models.py)
python3.8 manage.py makemigrations
# apply the discovered migrations
python3.8 manage.py migrate

```