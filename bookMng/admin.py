from django.contrib import admin

# Register your models here.


from .models import MainMenu
from .models import Book
from .models import Message
from .models import Comment
from .models import Rating

admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Rating)
