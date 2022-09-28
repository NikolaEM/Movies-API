from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=40)
    description =  models.TextField(max_length=3000)
    movie_cover = models.FileField(upload_to='')
    genre_choices = (
        ('A', 'Action'),
        ('C', 'Comedy'),
        ('D', 'Drama'),
        ('F', 'Fantasy'),
        ('H', 'Horror'),
    )
    genre = models.CharField(max_length=1, choices=genre_choices, default='')

    def __str__(self):
        return self.title