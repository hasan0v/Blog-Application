from django.contrib import admin
from .models import Post, Categorie, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Categorie)
admin.site.register(Profile)
