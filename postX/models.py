from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
 
User = settings.AUTH_USER_MODEL
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status=1)
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User, null = True, on_delete = models.SET_NULL, related_name = 'post_user' )
	post_txt = models.TextField(max_length = 7000)
	post_img = models.ImageField(upload_to = 'picx/%y%m%d')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateField(auto_now_add = True)
	updated = models.DateField(auto_now = True)
	users_like = models.ManyToManyField(User, related_name='posts_liked', blank=True)
	status = models.IntegerField(choices=STATUS, default=1)

	objects = models.Manager() # The default manager.
	published = PublishedManager() # custom manager.


	def get_absolute_url(self):
		return reverse('post_detail', args=[self.publish.year,	self.publish.month,	self.publish.day, self.id])
	
	class Meta:
		ordering = ('-publish',)
	def __str__ (self):
		#return self.post_txt.split()[0]
		return self.user.username

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cmnt_user')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	cmnt = models.CharField(max_length = 1000)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	class Meta:
		ordering = ('created',)
	def __str__(self):
		return f'{ self.user }: comments on {self.post}'
		
