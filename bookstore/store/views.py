from django.shortcuts import render, redirect
from .models import Book, Review, Cart, BookOrder
from django.contrib.auth.decorators import login_required
import geoip2.database
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

def index(request):
	return render(request,'base.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def store(request):
	fb_name = ''
	head = ''
	
	cart = Cart.objects.get(user = request.user, active = True)
	m = Book.objects.all().count()
	book = Book.objects.all()
	
	if request.user.is_authenticated():
		fb_name= request.user.first_name
		head = 'Welcome to the mystery book'

	# immediate response for geolocation
	reader = geoip2.database.Reader('geoapp/GeoLite2-City.mmdb')
	response = reader.city('122.172.69.71')
	print response.country.iso_code
	print response.city.name
	print response.country.name
	print response.postal.code
	print response.location.latitude
	print response.location.longitude
	reader.close()
	cart = BookOrder.objects.filter(cart=cart, isused = 1).order_by('cart').count()
	return render(request,'base.html',{'store' : m ,'facebook_name': fb_name , 'head': head , 'book':book, 'cart':cart})

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
				cart = Cart.objects.get(user= request.user , active = True)
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
	orders = BookOrder.objects.filter (cart = cart, isused= 1)
	total = 0
	count = 0
	for order in orders:
		count += order.quantity
		total += (order.book.price * order.quantity )

	return render (request,'store/cart.html',{'cart': orders,'total':total ,'count':count})

@csrf_exempt
@login_required
def navbar_cart_add (request,book_id):
	response = ''
	print "hello"
	if request.is_ajax():
		try:
			book = Book.objects.get(id= book_id)
		except Book.DoesNotExist:
			pass

		else:
			try:
				cart = Cart.objects.get(user = request.user, active = True)
				cart.add_to_cart(book_id)
			except Cart.DoesNotExist :
				new_cart = Cart.objects.create(
					user = request.user,
					active = True
					)
				new_cart.save()
				cart.add_to_cart(book_id)
		cart_count = BookOrder.objects.filter(cart=cart, isused = 1).order_by('cart').count()
	return HttpResponse(cart_count)


@csrf_exempt
@login_required
def navbar_cart_remove(request, book_id):
	try:
		book = Book.objects.get(id= book_id)
	except:
		pass

	else:
		cart = Cart.objects.get(user = request.user, active = True)
		cart.remove_from_cart(book_id)

		cart_count = BookOrder.objects.all().count()
		return HttpResponse(cart_count)



