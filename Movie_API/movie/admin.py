from django.contrib import admin
from .models import Genre

class Admin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    
admin.site.register(Genre)