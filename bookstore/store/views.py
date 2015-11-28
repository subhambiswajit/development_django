from django.shortcuts import render
from .models import Book


def index(request):
	return render(request,'index.html')

def store(request):
	m = Book.objects.all().count()
	print 'helloworld'
	
	return render(request,'store.html',{'store' : m})
