# Generated by Django 3.2.20 on 2024-11-08 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_friendlist_friendrequest_saveditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usergamedata',
            old_name='CustomUser',
            new_name='custom_user',
        ),
    ]
