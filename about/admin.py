from django.contrib import admin
from .models import Executive, Aboutus

# Register your models here.

@admin.register(Aboutus)
class AboutusAdmin(admin.ModelAdmin):
	pass

@admin.register(Executive)
class ExecutiveAdmin(admin.ModelAdmin):
	list_display = ['name', 'role', 'contact', 'hobby','pictur']