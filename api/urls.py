from django.urls import path
from .views import ArticlesListAPI, ArticlesDetailAPI, BooksListAPI, BooksDetailAPI

urlpatterns = [
    path('books/', BooksListAPI.as_view()),
    path('books/<int:pk>/', BooksDetailAPI.as_view()),
    path('articles/', ArticlesListAPI.as_view()),
    path('articles/<int:pk>/', ArticlesDetailAPI.as_view())
]
