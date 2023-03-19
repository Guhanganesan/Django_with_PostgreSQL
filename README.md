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

# GET Data (Model - Member)

1. Member.objects.all().values()
2. Member.objects.values_list('firstname')  => Specific columns
3. Member.objects.filter(firstname='Emil').values() => Specific Rows

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
