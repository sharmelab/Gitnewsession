from django.shortcuts import render

from django.http import HttpResponse

def home(request):
	return render(request,'home.html')
	#return HttpResponse('<marquee><h1>minicalci app created by SHRP</h1></marquee>')

