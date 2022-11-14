# Generated by Django 4.1.1 on 2022-10-09 21:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0011_alter_movie_dislikes_alter_movie_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='number_of_views',
            field=models.ManyToManyField(blank=True, related_name='movies_number_of_views', to=settings.AUTH_USER_MODEL),
        ),
    ]