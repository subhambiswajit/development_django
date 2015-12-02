from django.contrib import admin
from .models import Book, Author, Review

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','author','description')
class Authoradmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')
class Reviewadmin (admin.ModelAdmin):
	list_display = ('book','text')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, Authoradmin)
admin.site.register(Review, Reviewadmin)


# Register your models here.
