from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Theme(models.Model):
    name = models.CharField(max_length=150)
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Problem(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    answer = models.CharField(max_length=100)
    ball = models.IntegerField(default=0)
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    user_solver = models.TextField(default='')

    def __str__(self):
        return self.title