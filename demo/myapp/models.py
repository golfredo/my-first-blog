from django.db import models
from djangotoolbox.fields import ListField

# Create your models here.

class prueba(models.Model):
	title=models.CharField(max_length=200)
	text=models.TextField(max_length=200)
