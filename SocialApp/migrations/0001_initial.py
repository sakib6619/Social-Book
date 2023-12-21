# Generated by Django 4.2.7 on 2023-11-18 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('profile_image', models.ImageField(default='def.png', upload_to='profile_image/')),
                ('profile_cove', models.ImageField(default='cover.png', upload_to='profile_cover/')),
                ('bio', models.TextField(blank=True, max_length=120)),
                ('user_about', models.CharField(blank=True, max_length=300)),
                ('location', models.CharField(blank=True, max_length=300)),
                ('relationship', models.CharField(choices=[('single', 'single'), ('married', 'married'), ('divorced', 'divorced'), ('Others', 'Other')], max_length=150)),
                ('working', models.CharField(blank=True, max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
