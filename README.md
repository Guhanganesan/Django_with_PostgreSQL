# Django_with_PostgreSQL
1. Create Project: django-admin startproject Employee
2. cd Employee => Create App using 'python manage.py startapp myapp'
3. Register your app in settings.py file named 'myapp'
4. Add Templates directory in the settings.py file
5. Create a PostgreSQL database called Employee and set it up in the Django project’s settings.py file
6. Create urls.py and views.py in myapp
7. Create a models for Employee
8. Register models in admin.py


# Migrations

1. python manage.py makemigrations
2. python manage.py migrate

# Run App

1. python manage.py runserver

# Install PostgreSQL
1. pip install psycopg2 - OR
2. pip install psycopg2-binary -OR
3. python -m pip install Psycopg2

# References
1. Link: https://stackoverflow.com/questions/33215558/unable-to-install-psycopg2-on-windows
2. https://pythonguides.com/django-crud-example-with-postgresql/ 

