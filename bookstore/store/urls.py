from django.conf.urls import patterns, url
from store import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index$',views.index),
    url(r'^$', views.store),
    url(r'^count$',views.store),
    url(r'^book/details/(\d+)$',views.book_details, name="book_details")
)
