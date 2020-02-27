```

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

python3.8 manage.py startapp app_blog
python3.8 manage.py startapp app_projects

# add new apps to blog_core/settings.py --> INSTALLED_APPS
'app_blog',
'app_projects',
```