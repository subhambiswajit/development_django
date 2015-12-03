from django.contrib import admin
from .models import Book, Author, Review, Cart, BookOrder

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','author','description')
class Authoradmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')
class Reviewadmin (admin.ModelAdmin):
	list_display = ('book','text')
class BookOrderAdmin (admin.ModelAdmin):
	list_display = ('book','cart','quantity')
class CartAdmin(admin.ModelAdmin):
	list_display = ('user','active')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, Authoradmin)
admin.site.register(Review, Reviewadmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(BookOrder, BookOrderAdmin)


# Register your models here.
