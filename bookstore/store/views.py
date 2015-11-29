from django.shortcuts import render
from .models import Book


def index(request):
	return render(request,'index.html')

def store(request):
	m = Book.objects.all().count()
	
	if request.user.is_authenticated():
		fb_name= request.user.first_name
	# 	message = 'user is authenticated'

	return render(request,'store.html',{'store' : m ,'facebook_name': fb_name})
