from django.shortcuts import render, get_object_or_404
from .models import Executive, Aboutus

# Create your views here.

def aboutpage(request):
	cos = Executive.objects.filter(active=True)

	abt = get_object_or_404(Aboutus)
	
	return render(request, 'about/about.html', {'cos': cos, 'abt': abt})