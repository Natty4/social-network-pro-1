from django.db import models

# Create your models here.

class Executive(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	role = models.CharField(max_length=200, db_index=True)
	hobby = models.CharField(max_length=200, db_index=True)
	contact = models.CharField(max_length=200, db_index=True, null=True, blank=True )
	facebook = models.CharField(max_length=200, db_index=True, null=True, blank=True )
	twitter = models.CharField(max_length=200, db_index=True, null=True, blank=True )
	instagram = models.CharField(max_length=200, db_index=True, null=True, blank=True )
	pictur = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
	active = models.BooleanField(default=False)
	class Meta:
		ordering = ('name',)
	def __str__(self):
		return self.name

class Aboutus(models.Model):
	title = models.CharField(max_length=200)
	detail = models.TextField(blank=True)

	def __str__(self):
		return self.title
	
