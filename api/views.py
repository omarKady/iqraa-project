from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from articles.models import Article
from .serializers import BookSerializer, ArticleSerializer
# Create your views here.

class ListBooksAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListArticlesAPI(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer