# Django_with_PostgreSQL

1. Create Project: django-admin startproject Employee
2. cd Employee => Create App using 'python manage.py startapp myapp'
3. Register your app in settings.py file named 'myapp'
4. Add Templates directory in the settings.py file
5. Create a PostgreSQL database called Employee and set it up in the Django project’s settings.py file
6. Create urls.py and views.py in myapp
7. Create a models for Employee
8. Register models in admin.py

# Requirements

1. pip freeze > requirements.txt
2. pip install -r requirements.txt

# Migrations

1. python manage.py makemigrations
2. python manage.py migrate

# Super User

1. python manage.py createsuperuser

Username (leave blank to use 'macpro'): guhan
Email address: guhang990@gmail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

# Run App

1. python manage.py runserver

# Django Shell

1. python manage.py shell

# Git Ignore 

1. touch .gitignore
2. git config --global core.excludesfile ~/.gitignore_global

# Install PostgreSQL

1. pip install psycopg2 - OR
2. pip install psycopg2-binary -OR
3. python -m pip install Psycopg2

# Modules 

1. pip install schedule
2. pip install django-crontab
3. pip install django_google_sso
4. pip install pandas

# Django Google SSO

https://pypi.org/project/django-google-sso/

# References

1. Link: https://stackoverflow.com/questions/33215558/unable-to-install-psycopg2-on-windows
2. https://pythonguides.com/django-crud-example-with-postgresql/

# Basic Queries

1. Member.objects.all()
2. Member.objects.all().count()
3. Member.objects.all().delete()
4. Member(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail) => create
5. employees = Employee.objects.get(id=pk) =>  employees.EmpId = "some_value" => Update
6. Employee.objects.get(id=pk).delete() => For Single

# AND 

mydata = Member.objects.filter(lastname='Refsnes', id=2).values()

# OR 

mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()

# GET Data (Model - Member)

1. Member.objects.all().values()
2. Member.objects.values_list('firstname')  => Specific columns
3. Member.objects.filter(firstname='Emil').values() => Specific Rows
4. Member.objects.exclude(first_name__startswith = 'R')   => Objects that do not match the given lookup.
5. Member.objects.filter(first_name__startswith = 'R') | Member.objects.filter(last_name__startswith = 'S') 
6. Member.objects.filter(first_name__startswith = 'P') & Member.objects.filter(last_name__startswith = 'S') 
7. Member.objects.filter( first_name__startswith='A', last_name__startswith='S' )
8. Member.objects.all().count()
9. Member.objects.bulk_create([Member(first_name = 'Jai', last_name = 'Shah', mobile = '88888', email = 'shah@reddif.com'),Member(first_name = 'Tarak', last_name = 'Mehta', mobile = '9999', email = 'tarak@reddif.com'), Member(first_name = 'SuryaKumar', last_name = 'Yadav', mobile = '00000', email = 'yadav@reddif.com')])
10. Member.objects.all()[:4]      => Slicing
11. Member.objects.all()[:10:2]    => Negative indexing is not supported. However, using this.
12. Member.objects.filter(last_name__contains = 'Shar')

# Field Lookups

1. mydata = Member.objects.filter(lastname__icontains='ref').values() => WHERE lastname LIKE '%ref%'; 
2. mydata = Member.objects.filter(firstname__endswith='s').values() => WHERE firstname LIKE '%s';
3. mydata = Member.objects.filter(firstname__exact='Email').values() => WHERE firstname = 'Email';
4. mydata = Member.objects.filter(firstname__in=['Tobias', 'Linus', 'John']).values() => WHERE firstname IN ('Tobias', 'Linus', 'John');
5. mydata = Member.objects.filter(id__gt=3).values() => WHERE id > 3;
6. mydata = Member.objects.filter(id__gte=3).values() => WHERE id >= 3;
7. lt = less than, lte = less than or equal to
8. mydata = Member.objects.filter(id__range=(2, 4)).values() => WHERE id BETWEEN 2 AND 4;

# Filters

1. Add 10 dollars to all prices => {{ x|add:"10" }} dollars => if x=10; result 20 dollars
2. {{ fruits|slice:"1:4" }} => Get items 1, 2, and 3 from a list

# Order By

1. (ASC) mydata = Member.objects.all().order_by('firstname').values()  => SELECT * FROM members ORDER BY firstname;
2. (DESC) mydata = Member.objects.all().order_by('-firstname').values() => SELECT * FROM members ORDER BY firstname DESC;
3. mydata = Member.objects.all().order_by('lastname', '-id').values() => SELECT * FROM members ORDER BY lastname ASC, id DESC;
4. Member.objects.all().order_by('first_name','-mobile') => multiple
