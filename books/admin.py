from django.contrib import admin
from .models import Genre, Author, Book, Review

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
