from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    message = models.CharField(max_length=500)
    to_user = models.ForeignKey(User, blank=False, null=False, related_name="to_user_id", on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, blank=False, null=False, related_name="from_user_id", on_delete=models.CASCADE)
    message_date = models.DateField(auto_now=True)