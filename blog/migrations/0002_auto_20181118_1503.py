# Generated by Django 2.1.3 on 2018-11-18 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]