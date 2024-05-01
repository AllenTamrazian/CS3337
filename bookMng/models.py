from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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

    @property
    def ratings_average(self):
        average = self.ratings.all().aggregate(models.Avg('value'))['value__avg']
        if average:
            return f"{average:.2f}/5 from {self.ratings_count}"
        else:
            return "Unrated"

    @property
    def ratings_count(self):
        return len(self.ratings.all())

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    message = models.CharField(max_length=500)
    to_user = models.ForeignKey(User, blank=False, null=False, related_name="to_user_id", on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, blank=False, null=False, related_name="from_user_id", on_delete=models.CASCADE)
    message_date = models.DateField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    commenter_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, blank=False, null=False, on_delete=models.CASCADE, related_name='comments')

    @property
    def rating_value(self): # can't name this just 'rating', because that's the related name
        try:
            return f"{self.rating.get().value:.2f}/5"
        except Rating.DoesNotExist:
            return "Not rated"

    def __str__(self):
        return f"Comment by {self.commenter_name} on {self.book.name}"

class Rating(models.Model):
    value = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    book = models.ForeignKey(Book, blank=False, null=False, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.SET_NULL, related_name='rating')
