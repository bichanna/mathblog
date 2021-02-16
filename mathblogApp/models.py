"""
	math blog アプリ
	data model

	File name: models.py
	date: Feb 15, 2021
	written by Nobuharu Shimazu

"""


from django.db import models
from django.conf import settings
from django.utils import timezone



class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)
	image = models.ImageField(upload_to="images", blank=True)
	

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return str(self.title)