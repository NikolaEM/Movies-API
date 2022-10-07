from django.db import models
import os
from users.models import CustomUser

def get_file_path(instance, filename):
        return os.path.join('files', filename)

class Genre(models.Model):
    name = models.CharField(("name"), max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=40)
    description =  models.TextField(max_length=3000)
    movie_cover = models.FileField(upload_to=get_file_path, blank=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default="")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default= "")
    likes = models.ManyToManyField(CustomUser, related_name='movies_liked', blank=True)
    dislikes = models.ManyToManyField(CustomUser, related_name='movies_disliked', blank=True)

     
    def __str__(self):
        return self.title 

    @classmethod
    def like_movie(cls, user, pk):
        movie = cls.objects.get(id=pk)
        if movie.likes.filter(id=user.id).exists():
            movie.likes.remove(user)
        else:
            if movie.dislikes.filter(id=user.id).exists():
                movie.dislikes.remove(user)
            movie.likes.add(user)
        return movie

    @classmethod
    def dislike_movie(cls, user, pk):
        movie = cls.objects.get(id=pk)
        if movie.dislikes.filter(id=user.id).exists():
            movie.dislikes.remove(user)
        else:
            if movie.likes.filter(id=user.id).exists():
                movie.likes.remove(user)
            movie.dislikes.add(user)
        return movie