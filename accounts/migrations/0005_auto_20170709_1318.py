# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-09 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170709_0502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='details',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='year',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='organisation',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='projects',
            name='role',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='graduationdetails',
            name='course',
            field=models.CharField(choices=[('B.Sc.', 'B.Sc.'), ('B.E.', 'B.E.'), ('B.Tech.', 'B.Tech.'), ('B.A.', 'B.A.'), ('B.Com.', 'B.Com.')], max_length=20),
        ),
        migrations.AlterField(
            model_name='graduationdetails',
            name='stream',
            field=models.CharField(choices=[('Information Technology', 'Information Technology'), ('Computer Science', 'Computer Science'), ('Mechanical Engg', 'Mechanical Engg'), ('Electrical Engg', 'Electrical Engg'), ('Electronics and Communication', 'Electronics and Communication'), ('History', 'History'), ('Geography', 'Geography'), ('Economics', 'Economics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Maths', 'Maths')], max_length=20),
        ),
        migrations.AlterField(
            model_name='seniorsecondarydetails',
            name='stream',
            field=models.CharField(choices=[('Art', 'Arts'), ('Commerce', 'Commerce'), ('Science', 'Science')], max_length=20),
        ),
    ]
