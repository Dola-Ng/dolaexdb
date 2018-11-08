from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserDict(models.Model):
	DictName = models.CharField(max_length=20, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'pds')
	def __str__(self):
		return self.DictName

class Book(models.Model):
	bookname = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	genre = models.CharField(max_length=20)
	ratings = models.IntegerField()

	def __str__(self):
		return self.bookname