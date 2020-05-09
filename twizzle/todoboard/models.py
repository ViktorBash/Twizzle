from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


class Items(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(default=timezone.now)


class Shared_User(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    shared_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
