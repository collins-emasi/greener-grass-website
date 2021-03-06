# Generated by Django 3.2.5 on 2022-01-20 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_callbackrequest_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbackrequest',
            name='id_number',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='ID number must be 8 digits', regex='^\\d{8}$')]),
        ),
    ]
