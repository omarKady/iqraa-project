from django.shortcuts import render
from rest_framework import generics, permissions
from books.models import Book
from articles.models import Article
from .serializers import BookSerializer, ArticleSerializer
# Create your views here.

class BooksListAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BooksDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ArticlesListAPI(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticlesDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer