from django.contrib import admin

# Register your models here.


from .models import MainMenu
from .models import Book
from .models import Message
from .models import Comment

admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Message)
admin.site.register(Comment)
