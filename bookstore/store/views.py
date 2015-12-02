from django.shortcuts import render
from .models import Book


def index(request):
	return render(request,'base.html')

def store(request):
	fb_name = ''
	head = ''
	m = Book.objects.all().count()
	book = Book.objects.all()
	
	if request.user.is_authenticated():
		fb_name= request.user.first_name
		head = 'Welcome to the mystery book'
	# 	message = 'user is authenticated'

	return render(request,'base.html',{'store' : m ,'facebook_name': fb_name , 'head': head , 'book':book})
