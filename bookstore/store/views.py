from django.shortcuts import render, redirect
from .models import Book, Review, Cart, BookOrder
from django.contrib.auth.decorators import login_required
import geoip2.database


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

	m = Book.objects.all().count()
	book = Book.objects.all()
	
	if request.user.is_authenticated():
		fb_name= request.user.first_name
		head = 'Welcome to the mystery book'

	# immediate response for geolocation
	reader = geoip2.database.Reader('geoapp/GeoLite2-City.mmdb')
	response = reader.city('110.33.122.75')
	print response.country.iso_code
	print response.city.name
	print response.country.name
	print response.postal.code
	print response.location.latitude
	print response.location.longitude
	reader.close()

	q =  get_client_ip(request)
	
	ip = "141.211.0.0"

	ipgeobases = IPGeoBase.objects.by_ip (ip)
	if ipgeobases.exists ():
	    ipgeobase = ipgeobases [0]
	    print ipgeobase.country # Country
	    print ipgeobase.district # District (for the specified ip - Ural)
	    print ipgeobase.region # Region (Sverdlovsk region)
	    print ipgeobase.city # Settlement (Ekaterinburg)
	    print ipgeobase.ip_block # IP-block, which were (212.49.98.0 - 212.49.98.255)
	    print ipgeobase.start_ip, ipgeobase.end_ip # IP-block in a numeric format
	    print ipgeobase.latitude, ipgeobase.longitude # latitude and longitude

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




