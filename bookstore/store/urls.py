from django.conf.urls import patterns, url
from store import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index$',views.index),
    url(r'^$', views.store),
    url(r'^count$',views.store),
    url(r'^book/details/(\d+)$',views.book_details, name="book_details"),
    url(r'^navbar_add/(\d+)',views.navbar_cart_add, name= "navbar_add"),
     url(r'^navbar_remove/(\d+)',views.navbar_cart_remove, name= "navbar_remove"),
    url(r'^add/(\d+)',views.add_to_cart, name="add_to_cart"),
    url(r'^remove/(\d+)',views.remove_from_cart, name="remove_from_cart"),
    url(r'^cart/',views.cart, name="cart"),
)
