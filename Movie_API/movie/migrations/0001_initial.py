# Generated by Django 4.1.1 on 2022-09-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=3000)),
                ('movie_cover', models.FileField(upload_to='')),
                ('genre', models.CharField(choices=[('A', 'Action'), ('C', 'Comedy'), ('D', 'Drama'), ('F', 'Fantasy'), ('H', 'Horror')], default='', max_length=1)),
            ],
        ),
    ]
