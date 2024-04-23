from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Message


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            'message',
            'toUser',
        ]