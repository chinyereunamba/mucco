# Generated by Django 4.0.6 on 2022-07-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_delete_user_remove_account_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
