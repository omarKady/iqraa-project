from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.utils import timezone
from .models import Article, Comments
# Create your views here.

# Home Page View
class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.order_by('-id')[:10]
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ListAllArticlesView(ListView):
    model = Article
    queryset = Article.objects.order_by('-id')
    template_name = 'list_all_articles.html'

class AddCommentView(CreateView):
    model = Comments
    template_name = 'add_comment_to_article.html'
    fields = ('text',)
    
    # def get_initial(self, **kwargs):
    #     return {
    #         'comment_author': self.request.user,
    #         'related_article': Article.objects.get(pk=self.kwargs['pk'])
    #     }

    def form_valid(self, form, **kwargs):
        form.instance.related_article = Article.objects.get(pk=self.kwargs['pk'])
        form.instance.comment_author = self.request.user
        #form.instance.text = "Comment Test"
        return super(AddCommentView, self).form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy("home")