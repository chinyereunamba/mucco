# Generated by Django 4.0.6 on 2022-07-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, default='img-1.jgp', null=True, upload_to=''),
        ),
    ]
