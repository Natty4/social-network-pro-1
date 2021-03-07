from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse

# Create your models here.


SEX_CHOICE = (
	('M', 'Male'), 
	('F', 'Female')
)
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
	sex = models.CharField(choices = SEX_CHOICE, max_length = 1)
	photo_thumbnail = ImageSpecField(source='photo',processors = [ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})
	
	def get_absolut_url(self):
		return reverse('dashboard', kwargs={'pk':self.pk})
	
	def __str__(self):
		return f'Profile of {self.user.username}'