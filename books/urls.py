from django.urls import path
from .views import read_book_view, book_detail_view, comment_book_view

urlpatterns = [
    path('read/', read_book_view, name="read_books"),
    path('book_detail/<int:pk>', book_detail_view, name="book_detail"),
    path('book/<int:pk>/add_comment', comment_book_view, name="comment_book"),
]