from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        #return "/post/%i/" % self.id
        # return reverse('post_detail', args = [str(self.id)])
        return reverse('home')


class Comments(models.Model):
    related_article = models.ForeignKey(Article, on_delete= models.CASCADE, related_name='comments')
    text = models.TextField()
    comment_author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    # if you don't provide success_url attribute or get_success_url method on the view class
    # Django will try to get the URL to redirect from "get_absolute_url" method
    # on newly created object
    def get_absolute_url(self):
        article_id = self.related_article
        return reverse('article_detail_view', args = [str(article_id.id)])