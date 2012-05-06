from django.db import models

# Create your models here.

class Message(models.Model):

	author = models.CharField(max_length = 1000, blank = True)
	email = models.EmailField(blank = True)
	body = models.CharField(max_length = 20000, blank = True)
