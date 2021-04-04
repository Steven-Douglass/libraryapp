from django.contrib import admin

# Register your models here.

from .models import Address, Author, Book, BookAuthor, Library, Member

admin.site.register(Address)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Library)
admin.site.register(Member)