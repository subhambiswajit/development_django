from django.shortcuts import render
from .models import Book, Review
from django.contrib.auth.decorators import login_required


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
@login_required
def book_details(request,detail_id):
	
	m =''
	n=''
	no_review = False
	try:
		
		 	m= Review.objects.filter(book_id= detail_id)
	 	
	except Review.DoesNotExist:
	 	pass
	book = Book.objects.get(id = detail_id)
	print">>>>>>>>>>"
	print no_review
	return render(request,'store/detail.html',{'review':m, 'book':book, 'no_review': no_review})


