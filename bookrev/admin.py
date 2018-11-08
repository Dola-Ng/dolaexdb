from django.contrib import admin
from .models import UserDict
from .models import Book
# Register your models here.
admin.site.register(UserDict)
admin.site.register(Book)