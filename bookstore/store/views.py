from django.shortcuts import render
from .models import Book


def index(request):
	return render(request,'templates.html')

def store(request):
	m = Book.objects.all().count()
	return render(request,'store.html',{'store' : m})
