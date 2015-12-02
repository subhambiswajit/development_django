from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','author','description')
class Authoradmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, Authoradmin)


# Register your models here.
