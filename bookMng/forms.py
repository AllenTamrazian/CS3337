from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Message
from .models import Comment
from .models import Rating


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
            'to_user',
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'commenter_body'
        ]
        widgets = {
            'commenter_body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            'value'
        ]
