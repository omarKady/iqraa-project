from django.db.models import fields
from rest_framework import serializers
from books.models import Book
from articles.models import Article

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author', 'summary')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'author', 'body')