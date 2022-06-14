from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
	id = models.AutoField(primary_key=True)
	nama = models.CharField(max_length=100)
	npm = models.CharField(max_length=100)
	
	def __str__(self):
		return self.npm
