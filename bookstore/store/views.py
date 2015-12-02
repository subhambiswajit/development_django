from django.shortcuts import render, redirect
from .models import Book, Review, Cart, BookOrder
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
	
	return render(request,'store/detail.html',{'review':m, 'book':book, 'no_review': no_review})

@login_required
def add_to_cart(request, book_id):
	try:
		book = Book.objects.get(id= book_id)
	except Book.DoesNotExist:
		pass
	else:
		try:
			cart = Cart.objects.get(user= request.user , active = True)
			
			
		except:
				create_cart = Cart.objects.create(
					user = request.user
					)
				create_cart.save()
		cart.add_to_cart(book_id)		
	return redirect('cart')
@login_required
def remove_from_cart (request, book_id):
	try:
		book = Book.objects.get(id= book_id)
	except Book.DoesNotExist:
		pass
	else:
	   	cart = Cart.objects.get(user = request.user, active= True)
	   	cart.remove_from_cart(book_id)
   	return redirect('cart')

@login_required
def cart(request):
	cart = Cart.objects.get(user= request.user, active= True)
	orders = BookOrder.objects.filter (cart = cart)
	total = 0
	count = 0
	for order in orders:
		count += order.quantity
		total += (order.book.price * order.quantity )
	return render (request,'store/cart.html',{'cart': orders,'total':total ,'count':count})




