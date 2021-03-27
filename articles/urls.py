from django.urls import path

from .views import ArticleListView, ArticleDetailView, ListAllArticlesView, AddCommentView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view() , name='article_detail_view'),
    path('all_articles/', ListAllArticlesView.as_view(), name='list_all_articles'),
    path('article/<int:pk>/add_comment', AddCommentView.as_view(), name='add_comment'),
]