# Generated by Django 5.1 on 2024-08-27 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='books',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course'),
        ),
    ]
