# Generated by Django 4.2.7 on 2023-11-18 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0004_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='LikePost',
        ),
    ]