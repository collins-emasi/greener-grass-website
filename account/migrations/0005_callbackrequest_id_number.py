# Generated by Django 3.2.5 on 2022-01-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_username_callbackrequest_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbackrequest',
            name='id_number',
            field=models.CharField(default=37174841, max_length=9, unique=True),
            preserve_default=False,
        ),
    ]
