from distutils.command.upload import upload
from email.policy import default
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import date, datetime
# Create your models here.

class Profile(models.Model): 
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    facebook_url=models.CharField(max_length=255, null=True, blank=True)
    instagram_url=models.CharField(max_length=255, null=True, blank=True)
    twitter_url=models.CharField(max_length=255, null=True, blank=True)
    prof_pic = models.ImageField(null=True, blank=True, upload_to="images/prof_pics")
    follower = models.ManyToManyField(User, blank=True, related_name='blog_profile')
    # follow = models.ManyToManyField(User, related_name='blog_user')


    def total_follower(self):
        return self.follower.count()


    def __str__(self):
        return str(self.user)

class Post (models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextField(blank=True, null=False)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="Coding")
    snippet=RichTextField(blank=True, null=False, max_length=100)
    likes = models.ManyToManyField(User, related_name='blogapp_post')

    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + ' | ' + str(self.author) 
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})

class Categorie (models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
        # return reverse('post_detail', kwargs={"pk": self.pk})






