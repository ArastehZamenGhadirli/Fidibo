from django.contrib import admin
from book.models import *
# Register your models here.


admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Publisher)