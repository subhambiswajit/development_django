from django.conf.urls import patterns, url
from store import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index),
    url(r'^count$',views.store),
)
