# Generated by Django 4.0.6 on 2022-07-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_category_date_created_newsletter_date_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
