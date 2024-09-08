from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Catergory(models.Model):
    name = models.CharField(max_length=100)
    content =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name




class Skills(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return self.name


class Trainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trainer',default='default.jpg')
    Skills = models.ManyToManyField(Skills)
    description = models.TextField()
    twitter = models.CharField(max_length=120,default='twitter')
    facebook = models.CharField(max_length=120,default='facebook')
    instagram = models.CharField(max_length=120,default='instagram')
    linkedin = models.CharField(max_length=120,default='linkedin')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.user.username
    

class Courses(models.Model):
    name = models.CharField(max_length=120)
    fee = models.FloatField(default=10.5)
    capacity = models.IntegerField(default=10)
    schedule = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='course',default='images.png')
    Trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    content = models.TextField()
    Catergory = models.ManyToManyField(Catergory)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name