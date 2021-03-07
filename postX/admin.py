from django.contrib import admin
from .models import Post, Comment
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['user','updated','post_img']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['user','cmnt', 'updated']