# Generated by Django 3.2.8 on 2022-09-06 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweetvillaApp', '0006_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]