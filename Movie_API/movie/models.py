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
     
    def __str__(self):
        return self.title 