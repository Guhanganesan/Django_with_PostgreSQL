# Generated by Django 3.2.17 on 2023-03-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_employee_empid'),
    ]

    operations = [
        migrations.CreateModel(
            name='EceStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('pass_word', models.CharField(max_length=200)),
            ],
        ),
    ]
