from django.contrib import admin

from .models import *



admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Borrowing)
admin.site.register(Genre)