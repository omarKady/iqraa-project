from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('read_books')


class Comments(models.Model):
    related_book = models.ForeignKey(Book, on_delete= models.CASCADE, related_name='comments')
    text = models.TextField()
    comment_author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        book_id = self.related_book
        return reverse('book_detail', args = [str(book_id.id)])