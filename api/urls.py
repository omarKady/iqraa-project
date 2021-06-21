from django.urls import path
from .views import ListBooksAPI, ListArticlesAPI

urlpatterns = [
    path('books/', ListBooksAPI.as_view()),
    path('articles/', ListArticlesAPI.as_view())
]
