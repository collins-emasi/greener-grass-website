# Generated by Django 3.2.5 on 2022-01-19 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_callbackrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='callbackrequest',
            old_name='user_name',
            new_name='username',
        ),
    ]
