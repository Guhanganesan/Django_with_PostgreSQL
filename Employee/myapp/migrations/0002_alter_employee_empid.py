# Generated by Django 3.2.17 on 2023-03-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpId',
            field=models.CharField(max_length=5),
        ),
    ]
