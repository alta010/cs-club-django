# Generated by Django 2.2.4 on 2020-08-18 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0008_auto_20200818_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='hasBeenRead',
            new_name='unread',
        ),
    ]
